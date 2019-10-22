#!/bin/bash
if [ "$1" == "exec" ]
    then
        if [ -n "$INPUT_DIR" ]
            then
                echo "Changing into $INPUT_DIR"
                cd "$INPUT_DIR"
        fi
        jupytext --to ipynb --execute "${@:2}"
elif [ "$1" == "notebook" ]
    then
        jupyter notebook
fi
