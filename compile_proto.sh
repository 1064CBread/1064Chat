#!/usr/bin/env bash

# the sleeps below are for IDEs, syserr and sysout flushing may align strangely

protobuf_name="protobuf"
sourcedir="src"
importdir="$sourcedir/${protobuf_name}_imports"
outputdir="$sourcedir/generated_$protobuf_name"
protodir="$sourcedir/$protobuf_name"
fileselector=( $protodir/**.proto )

if test -n "$(find "$fileselector" -print -quit 2>/dev/null)"; then
    echo "File(s) to compile:" >&2
    for i in "${fileselector[@]}"; do
        echo -e "\t$i" >&2
    done
    echo Found files to compile, running protoc now... >&2
    sleep 0.1
else
    echo No files to compile! '('"Looked in $protodir"')' >&2
    exit 1
fi

mkdir -p "$outputdir"
protoc --proto_path="$importdir" --proto_path="$protodir" --python_out="$outputdir" "$fileselector" 2>&1
sleep 0.1
echo "Finished successfully." >&2
