USE default;

CREATE TABLE IF NOT EXISTS events (
    event_time DateTime DEFAULT now(),
    event_type String,
    value Int32
) ENGINE = MergeTree()
ORDER BY event_time;
