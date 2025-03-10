def aggregate_hourly(events_df):
    result = (
        events_df.resample("h", on="event_time")
        .agg(
            event_count=("event_type", "count"),
            value_sum=("value", "sum"),
            value_avg=("value", "mean"),
        )
        .fillna(0)
        .reset_index()
    )

    result["value_avg"] = result["value_avg"].round(2)
    return result


def aggregate_by_event_type(events_df):
    return (
        events_df.groupby("event_type")
        .agg(event_count=("event_type", "count"), value_sum=("value", "sum"))
        .reset_index()
    )
