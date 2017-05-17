#!/bin/bash

docker rm -f doc-project
rm -rf site
asciibinder package
mkdir site
cp -r _package/main/ site/

# These two lines work around a known issue with asciibinder
mv -f site/main/* site/ > /dev/null 2>&1
mv -f site/latest/* site/ > /dev/null 2>&1

docker run --name doc-project -p 8080:80 -v /home/bexelbie/Repositories/personal/bexelbie-talks-demos/OSCAL.2017.Dont.Write.It.All/world/builder/site:/usr/share/nginx/html:Z -d nginx
