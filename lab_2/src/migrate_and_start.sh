#!/bin/sh

echo "⏳"
while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 1
done

echo "✅"
flask db upgrade

echo "🚀"
exec flask run --host=0.0.0.0
