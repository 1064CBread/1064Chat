#!/usr/bin/env bash

# the sleeps below are for IDEs, syserr and sysout flushing may align strangely

sourcedir="protobuf"
importdir="${sourcedir}_imports"
outputdir="generated_$sourcedir"
fileselector=( $sourcedir/**.proto )


if test -n "$(find "$fileselector" -print -quit 2>/dev/null)"; then
    echo Found files to compile, running protoc now... >&2
    sleep 0.1
else
    echo No files to compile! >&2
    exit 1
fi

mkdir -p "$outputdir"
protoc --proto_path="$importdir" --proto_path="$sourcedir" --python_out="$outputdir" "$fileselector" 2>&1
sleep 0.1
echo "Finished successfully." >&2
