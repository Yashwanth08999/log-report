#!/bin/bash
set -euo pipefail

mkdir -p /logs/verifier

if pytest /tests/test_outputs.py \
    --json-report \
    --ctrf /logs/verifier/ctrf.json \
    -rA
then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
fi
