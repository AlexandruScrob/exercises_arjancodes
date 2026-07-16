from datetime import datetime
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

FOOD_CSV = Path("food.csv")
ACTIVITIES_CSV = Path("activities.csv")


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


@dataclass
class Entry:
    description: str
    calories: int
    date: str = field(default_factory=today)


def append_entry(filename: Path, entry: Entry) -> None:
    with open(filename, "a") as f:
        f.write(f"{entry.date},{entry.description},{entry.calories}\n")
    print(f"Appended food: {entry.description} ({entry.calories} kcal) on {entry.date}")


def read_entries(filename: Path) -> Iterator[Entry]:
    with open(filename) as f:
        for line in f:
            parts = line.strip().split(",")
            yield Entry(description=parts[1], calories=int(parts[2]), date=parts[0])


def run_day_summary(date: str) -> None:
    food: list[Entry] = list(read_entries(FOOD_CSV))
    activity: list[Entry] = list(read_entries(ACTIVITIES_CSV))

    food_total = sum(entry.calories for entry in food if entry.date == date)
    activity_total = sum(entry.calories for entry in activity if entry.date == date)
    net = food_total - activity_total

    print(f"\nSummary for {date}")
    print(f"  🍎 Food:     {food_total} kcal")
    print(f"  🏃 Activity: {activity_total} kcal")
    print(f"  ⚖️  Net:       {net} kcal")


append_entry(FOOD_CSV, Entry("Banana", 100))
append_entry(ACTIVITIES_CSV, Entry("Running", 300))
run_day_summary(today())
