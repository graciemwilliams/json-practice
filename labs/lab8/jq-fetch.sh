#!/bin/bash

cat aviation.json | jq -r '.[0:6] | .[].receiptTime'

