#!/usr/bin/env bash

sourcedir="protobuf"
importdir="${sourcedir}_imports"
outputdir="generated_$sourcedir"
fileselctor="$sourcedir/"'**.proto'

if test -n "$(find "$fileselector" -print -quit 2>/dev/null)"; then
    echo Found files to compile, running protoc now...
else
    echo No files to compile!
    exit 1
fi

protoc --proto_path="$importdir" --python_out="$outputdir" "$fileselector"

