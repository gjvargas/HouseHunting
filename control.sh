#!/bin/bash

NUM_TRIALS=50
NUM_NESTS=20
MAX_NUM_ANTS=2000
NUM_ANTS_STEP_SIZE=50
NUM_STEPS=$(($MAX_NUM_ANTS / $NUM_ANTS_STEP_SIZE))

for i in {1..50}
do
    numAnts=$(($i * $NUM_ANTS_STEP_SIZE))
    python run.py $NUM_TRIALS $numAnts $NUM_NESTS Ant Nest &
done
