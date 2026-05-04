from event import Event


class EventStore:
    def __init__(self) -> None:
        self._events: list[Event] = []

    def append(self, event: Event) -> None:
        self._events.append(event)

    def get_all_events(self) -> list[Event]:
        return list(self._events)
