#!/bin/sh
poetry install --no-root

exec "$@"