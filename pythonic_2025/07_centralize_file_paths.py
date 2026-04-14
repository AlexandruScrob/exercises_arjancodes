from datetime import datetime
from dataclasses import dataclass, field
from pathlib import Path

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


def run_day_summary(date: str) -> None:
    food: list[int] = []
    try:
        with open(FOOD_CSV) as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == date:
                    food.append(int(parts[2]))

    except FileNotFoundError:
        print("Could not read food.csv")

    activity: list[int] = []
    try:
        with open(ACTIVITIES_CSV) as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == date:
                    activity.append(int(parts[2]))

    except FileNotFoundError:
        print("Could not read activities.csv")

    food_total = sum(food)
    activity_total = sum(activity)
    net = food_total - activity_total

    print(f"\nSummary for {date}")
    print(f"  🍎 Food:     {food_total} kcal")
    print(f"  🏃 Activity: {activity_total} kcal")
    print(f"  ⚖️  Net:       {net} kcal")


append_entry(FOOD_CSV, Entry("Banana", 100))
append_entry(ACTIVITIES_CSV, Entry("Running", 300))
run_day_summary(today())
