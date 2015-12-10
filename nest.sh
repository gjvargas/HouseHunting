#!/bin/bash

NUM_TRIALS=50
NUM_ANTS=500
MAX_NUM_NESTS=200
NUM_NESTS_STEP_SIZE=5
NUM_STEPS=$(($MAX_NUM_NESTS / $NUM_NESTS_STEP_SIZE))

for ((i=$NUM_NESTS_STEP_SIZE; i <= $MAX_NUM_NESTS; i+=$NUM_NESTS_STEP_SIZE))
do
    python run.py $NUM_TRIALS $NUM_ANTS $i Ant Nest &
done
