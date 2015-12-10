#!/bin/bash

NUM_TRIALS=50
NUM_NESTS=50
MAX_NUM_ANTS=2000
NUM_ANTS_STEP_SIZE=50
NUM_STEPS=$(($MAX_NUM_ANTS / $NUM_ANTS_STEP_SIZE))

for ((i=$NUM_ANTS_STEP_SIZE; i <= $MAX_NUM_ANTS; i+=$NUM_ANTS_STEP_SIZE))
do
    python run.py $NUM_TRIALS $i $NUM_NESTS Ant Nest &
    python run.py $NUM_TRIALS $i $NUM_NESTS Ant NonbinaryNest &
    python run.py $NUM_TRIALS $i $NUM_NESTS Ant DistanceNest &
    python run.py $NUM_TRIALS $i $NUM_NESTS Ant NonbinaryDistanceNest &
done
