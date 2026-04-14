from datetime import datetime
import os


def log_food(item: str, calories: int, date: str | None = None) -> None:
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    with open("food.csv", "a") as f:
        f.write(f"{date},{item},{calories}\n")
    print(f"Appended food: {item} ({calories} kcal) on {date}")


def log_activity(activity: str, calories_burned: int, date: str | None = None) -> None:
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    with open("activities.csv", "a") as f:
        f.write(f"{date},{activity},{calories_burned}\n")
    print(f"Appended activity: {activity} ({calories_burned} kcal) on {date}")


def run_day_summary(date: str) -> None:
    food: list[int] = []
    if os.path.exists("food.csv"):
        with open("food.csv") as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == date:
                    food.append(int(parts[2]))

    else:
        print("Could not read food.csv")

    activity: list[int] = []
    if os.path.exists("activities.csv"):
        with open("activities.csv") as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == date:
                    activity.append(int(parts[2]))

    else:
        print("Could not read activities.csv")

    food_total = sum(food)
    activity_total = sum(activity)
    net = food_total - activity_total

    print(f"\nSummary for {date}")
    print(f"  🍎 Food:     {food_total} kcal")
    print(f"  🏃 Activity: {activity_total} kcal")
    print(f"  ⚖️  Net:       {net} kcal")


log_food("Banana", 100)
log_activity("Running", 300)
run_day_summary(datetime.now().strftime("%Y-%m-%d"))
