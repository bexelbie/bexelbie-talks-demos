#!/usr/bin/perl

while (<>) {
    chomp;
    if ($_ eq "") {
        next;
    } elsif (s/^# //) {
        # Found the Title
        $title = $_;
        $body .= "<h1>".$_."</h1>\n";
    } elsif (s/^## //) {
        $body .= "<h2>".$_."</h2>\n";
    } else {
        $body .= "<p>".$_."</p>\n";
    }
}

print <<EOF;
<html>
<head>
<title>$title</title>
</head>
<body>
$body
</body>
</html>
EOF
