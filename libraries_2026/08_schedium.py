from datetime import datetime

from schedium import Between, Every, Job, JobDidNotRun, Scheduler


def sync_orders() -> str:
    print("Syncing orders...")
    return "orders synced"


def send_daily_report() -> str:
    print("Sending daily report...")
    return "report sent"


def main() -> None:
    scheduler = Scheduler()

    working_hours_trigger = Every(unit="minute", interval=15) & Between(
        unit="hour_of_day",
        start=9,
        end=17,
    )

    scheduler.append(
        Job(
            func=sync_orders,
            trigger=working_hours_trigger,
            name="sync-orders",
        )
    )

    scheduler.append(
        Job(
            func=send_daily_report,
            trigger=Every(unit="day", interval=1),
            name="daily-report",
        )
    )

    # In a real app, you would usually call scheduler.run_pending()
    # inside a loop. For a video demo, fixed timestamps are easier.
    moments = [
        datetime(2026, 7, 1, 8, 45),  # before working hours
        datetime(2026, 7, 1, 9, 0),  # sync_orders runs
        datetime(2026, 7, 1, 9, 0, 30),  # same time bucket: deduplicated
        datetime(2026, 7, 1, 9, 15),  # sync_orders runs again
        datetime(2026, 7, 1, 18, 0),  # outside working hours
    ]

    for moment in moments:
        print(f"\nRunning scheduler at {moment.time()}")

        results = scheduler.run_pending(now=moment)

        for job, result in zip(scheduler.jobs, results):
            if result is JobDidNotRun:
                print(f"{job.name}: not due")
            else:
                print(f"{job.name}: {result}")


if __name__ == "__main__":
    main()
