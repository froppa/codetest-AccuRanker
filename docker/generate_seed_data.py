import argparse
import random
from datetime import datetime, timedelta

EVENT_TYPES = ["click", "view", "purchase", "error", "signup"]
START_TIME = datetime(2025, 1, 1, 0, 0, 0)
DAYS_SPAN = 10


def main(output_file: str, rows: int):
    """Generate random event data and write to an SQL file."""

    timestamps = [
        START_TIME
        + timedelta(
            days=random.randint(0, DAYS_SPAN),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59),
        )
        for _ in range(rows)
    ]

    timestamps.sort()

    values = [
        f"('{ts.strftime('%Y-%m-%d %H:%M:%S')}', '{random.choice(EVENT_TYPES)}', {random.randint(1, 100)})"
        for ts in timestamps
    ]

    sql = f"INSERT INTO events (event_time, event_type, value) VALUES {', '.join(values)};"

    with open(output_file, "w") as f:
        f.write(sql)

    print(f"✅ Successfully generated {output_file} with {rows} rows")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate sample data for ClickHouse")
    parser.add_argument(
        "--output-file", type=str, default="seed.sql", help="SQL output file"
    )
    parser.add_argument(
        "--rows", type=int, default=1000, help="Number of rows to generate"
    )

    args = parser.parse_args()
    main(args.output_file, args.rows)
