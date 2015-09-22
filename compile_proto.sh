#!/usr/bin/env bash

sourcedir="protobuf"
importdir="${sourcedir}_imports"
outputdir="generated_$sourcedir"
fileselector=( $sourcedir/**.proto )


if test -n "$(find "$fileselector" -print -quit 2>/dev/null)"; then
    echo Found files to compile, running protoc now...
else
    echo No files to compile!
    exit 1
fi

mkdir -p "$outputdir"
protoc --proto_path="$importdir" --proto_path="$sourcedir" --python_out="$outputdir" "$fileselector"
echo "Finished successfully."

