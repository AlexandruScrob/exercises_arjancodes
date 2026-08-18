from __future__ import annotations

from dataclasses import dataclass, field
from math import sqrt
from typing import Protocol

# MISSING = object()  # 6.


@dataclass(frozen=True)
class Coordinates:
    x: float
    y: float

    def distance_to(self, other: Coordinates) -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


@dataclass(frozen=True)
class GeoFence:
    name: str


@dataclass
class Route:
    start: Coordinates | None = None
    destination: Coordinates | None = None
    avoid_zones: list[GeoFence] = field(default_factory=list[GeoFence])

    def avoid(self, zone: GeoFence) -> None:
        self.avoid_zones.append(zone)


@dataclass(frozen=True)
class DroneTelemetry:
    drone_id: str
    location: Coordinates | None
    battery_level: int | None
    max_wind_speed: int | None


@dataclass(frozen=True)
class ReadyDrone:
    drone_id: str
    location: Coordinates
    battery_level: int
    max_wind_speed: int


@dataclass(frozen=True)
class OfflineDrone:
    drone_id: str


@dataclass(frozen=True)
class ConnectedDrone:
    drone_id: str
    battery_id: int


@dataclass
class Delivery:
    destination: Coordinates
    required_battery: int
    avoid_zones: list[GeoFence] | None = None


@dataclass
class WeatherReport:
    wind_speed: int


class RouteRejected(Exception):
    pass


class Diagnostics(Protocol):
    def record(self, message: str) -> None: ...


class RouteDiagnostics:
    def record(self, message: str) -> None:
        print(f"[diagnostics] {message}")


class NullDiagnostics:
    def record(self, message: str) -> None:
        pass


def prepare_drone(telemetry: DroneTelemetry) -> ReadyDrone:
    if telemetry.location is None:
        raise ValueError("Drone has no GPS location.")

    if telemetry.battery_level is None:
        raise ValueError("Drone has no battery reading.")

    if telemetry.max_wind_speed is None:
        raise ValueError("Drone has no wind safety rating.")

    return ReadyDrone(
        drone_id=telemetry.drone_id,
        location=telemetry.location,
        battery_level=telemetry.battery_level,
        max_wind_speed=telemetry.max_wind_speed,
    )


def estimate_battery_usage(start: Coordinates, destination: Coordinates) -> int:
    return round(start.distance_to(destination) * 10)


@dataclass(frozen=True)
class RouteFailed:
    reason: str


type RouteResult = Route | RouteFailed  # 7.


def assign_delivery(
    telemetry: ReadyDrone,
    delivery: Delivery,
    weather: WeatherReport,
    diagnostics: Diagnostics,
) -> RouteResult:
    diagnostics.record("Starting route assignment")

    route = Route()

    route.start = telemetry.location

    if weather.wind_speed > telemetry.max_wind_speed:
        diagnostics.record("Too windy for this drone")
        return RouteFailed(reason="Too windy for this drone")  # 7.

    for zone in delivery.avoid_zones:
        route.avoid(zone)

    estimated_usage = estimate_battery_usage(
        telemetry.location,
        delivery.destination,
    )

    if telemetry.battery_level < estimated_usage:
        diagnostics.record("Battery too low")
        raise RouteRejected("Battery too low")

    route.destination = delivery.destination

    diagnostics.record("Route assigned")

    return route


def main() -> None:
    telemetry = DroneTelemetry(
        drone_id="drone-1",
        location=Coordinates(0, 0),
        battery_level=80,
        max_wind_speed=35,
    )

    delivery = Delivery(
        destination=Coordinates(3, 4),
        required_battery=50,
        avoid_zones=[GeoFence("city-center")],
    )

    weather = WeatherReport(wind_speed=20)
    # diagnostics = NullDiagnostics()
    diagnostics = RouteDiagnostics()

    drone = prepare_drone(telemetry)

    route = assign_delivery(drone, delivery, weather, diagnostics)

    print(route)


if __name__ == "__main__":
    main()
