#!/bin/bash
if [ "$1" == "exec" ]
    then
        bash -c "jupytext --to ipynb --execute ${@:2}"
elif [ "$1" == "notebook" ]
    then
        bash -c "jupyter notebook"
fi