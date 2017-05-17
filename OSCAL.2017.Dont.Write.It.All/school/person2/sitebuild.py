#!/usr/bin/python3

import csv
import os

menu = ""
with open('config') as tsv:
    for line in csv.reader(tsv, delimiter='\t'):
        if not menu:
            menu = "<a href=\"index.html\">"+line[0]+"</a>\n"
            files = [line[1]]
        else:
            menu += "<a href=\""+line[1]+"\">"+line[0]+"</a>\n"
            files.append(line[1])

# CSS
def getCSS():
    return("""<style>
.sidenav {
    height: 100%;
    width: 15%;
    position: fixed;
    top: 0;
    left: 0;
    background-color: #111;
    z-index: 1;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
    float:left;
}

.sidenav a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 25px;
    color: #818181;
    display: block;
    transition: 0.3s;
}

.sidenav a:hover, .offcanvas a:focus{
    color: #f1f1f1;
}

#main {
    transition: margin-left .5s;
    padding: 16px;
    float:right;
    width: 80%;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
""")

# CSS
def getMenu():
    return("<div id=\"mySidenav\" class=\"sidenav\">\n" + menu + "</div>\n")

for index, filename in enumerate(files):
    with open(filename) as file_input:
        if index == 0:
            filename = "index.html"
        with open("output/"+filename, "w") as file_output:
            for line in file_input:
                if line == "</head>\n":
                    file_output.write(getCSS())
                file_output.write(line)
                if line == "<body>\n":
                    file_output.write(getMenu())
                    file_output.write("<div id=\"main\">")
                if line == "</body>\n":
                    file_output.write("</div")
