#!/bin/bash

if [ ! -d "output" ]; then
    mkdir output;
fi

basename -s .format `ls *.format` | xargs -I FILE sh -c "./format2html.pl FILE.format > FILE.html"
./sitebuild.py
cd output
echo "open http://localhost:8080"
../server
