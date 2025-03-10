FROM python:3.11 as builder

WORKDIR /app

COPY generate_seed_data.py .

RUN python /app/generate_seed_data.py --output-file=/app/seed_data.sql

FROM clickhouse/clickhouse-server:latest

COPY --from=builder /app/seed_data.sql /app/seed_data.sql

CMD ["/bin/sh", "-c", "/entrypoint.sh & sleep 5 && clickhouse-client --host=clickhouse-server --user=root --password=root --queries-file /app/seed_data.sql; echo 'Succesfully Inserted seed data'"]
