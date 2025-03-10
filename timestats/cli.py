import os
from dotenv import load_dotenv
from timestats.clients.clickhouse import ClickHouseClient
from timestats.aggregations import (
    aggregate_hourly,
    aggregate_by_event_type,
)
from prettytable import PrettyTable


def display_table(df, title):
    table = PrettyTable()
    table.field_names = df.columns.tolist()

    for row in df.itertuples(index=False):
        table.add_row(row)

    print(f"\n{title}\n" + "=" * len(title))
    print(table)


def main():
    load_dotenv()

    client = ClickHouseClient(
        host=os.getenv("DATABASE_HOST"),
        database=os.getenv("DATABASE_NAME"),
    )

    events = client.fetch_events()

    display_table(aggregate_hourly(events), "Hourly Aggregation")
    display_table(aggregate_by_event_type(events), "Event Type Grouping")


if __name__ == "__main__":
    main()
