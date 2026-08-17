from geopy.distance import geodesic
from geopy.exc import GeocoderServiceError, GeocoderTimedOut
from geopy.geocoders import Nominatim


def geocode_address(geolocator: Nominatim, address: str):
    try:
        location = geolocator.geocode(address, exactly_one=True, timeout=10)
    except (GeocoderTimedOut, GeocoderServiceError) as error:
        print(f"Could not geocode {address!r}: {error}")
        return None

    if location is None:
        print(f"Could not find location for {address!r}")
        return None

    return location


def main() -> None:
    geolocator = Nominatim(user_agent="arjancodes-geopy-demo")

    amsterdam = geocode_address(geolocator, "Amsterdam Centraal, Netherlands")
    rotterdam = geocode_address(geolocator, "Rotterdam Centraal, Netherlands")

    if amsterdam is None or rotterdam is None:
        return

    print(f"Amsterdam: {amsterdam.latitude}, {amsterdam.longitude}")
    print(f"Rotterdam: {rotterdam.latitude}, {rotterdam.longitude}")

    distance = geodesic(
        (amsterdam.latitude, amsterdam.longitude),
        (rotterdam.latitude, rotterdam.longitude),
    )

    print(f"Distance: {distance.kilometers:.1f} km")

    reverse_location = geolocator.reverse(
        (amsterdam.latitude, amsterdam.longitude),
        exactly_one=True,
        timeout=10,
    )

    if reverse_location:
        print(f"Reverse geocoded address: {reverse_location.address}")


if __name__ == "__main__":
    main()
