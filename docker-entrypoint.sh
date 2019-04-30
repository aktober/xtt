#!/usr/bin/env bash

echo "DB UPGRADE"
until flask db upgrade
  do
      echo "UPGRADE: Waiting for mysql ready..."
      sleep 2
  done

flask run --host 0.0.0.0 --port 5000