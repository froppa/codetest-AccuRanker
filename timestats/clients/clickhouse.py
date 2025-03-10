import os
import clickhouse_connect
import pandas as pd


class ClickHouseClient:
    def __init__(self, host: str, database: str):
        self.host = os.getenv("DATABASE_HOST", host)
        self.database = os.getenv("DATABASE_NAME", database)
        self.username = os.getenv("DATABASE_USER", "root")
        self.password = os.getenv("DATABASE_PASSWORD", "root")

        self.client = clickhouse_connect.get_client(
            host=self.host,
            database=self.database,
            username=self.username,
            password=self.password,
        )

    """
    Fetches all events from Clickhouse
    """

    def fetch_events(self):
        query = f"SELECT event_time, event_type, value FROM events"
        result = self.client.query_df(query)

        result["event_time"] = pd.to_datetime(result["event_time"])
        return result
