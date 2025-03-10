# Time Series Data Analysis with Clickhouse

# Setup

```bash
pip install -e .
```

# Usage

```bash
docker compose up -d; timestats
```

## To Do:

- [x] On the first run, initialize the database by creating an events table with the following schema:
  - `event_time`: The timestamp when the event occurred.
  - `event_type`: A category label for the event
    - enum: (click|view|purchase)
  - `value`: A numerical metric associated with the event.
- [x] Populate the events table with sample data spanning at least 3 days.
  - Multiple events per hour.
  - All event_types are represented.
  - Value must be non-uniform to allow meaningful aggregations.
- [x] Display and aggregate events pr. hour (resampled) using PrettyTable

### Data Retrieval & Transformation:

- **Data Retrieval:**

  - Connect to ClickHouse.
  - Query all data from the events table and load it into a Pandas DataFrame.
  - Parse the event_time column as a datetime object.

- **Time-based Aggregations:**
  - **Hourly Aggregation:**
    - Resample the data to compute for each hour:
      - Total number of events.
      - Sum of the value field.
      - Average of the value field.
  - **Event Type Grouping:**
    - Group the data by event_type (regardless of time) to compute:
      - Total count of events for each type.
      - Total sum of the value field for each type.
