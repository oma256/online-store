FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN apk update && \
    apk add --no-cache gcc musl-dev libffi-dev linux-headers  postgresql-dev && \
    pip install --no-cache-dir -r /app/requirements.txt
RUN mkdir -p /app/logs
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
