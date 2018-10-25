#!/bin/bash
#enput encoding here
FROM_ENCODING="binary"
#output encoding(UTF-8)
TO_ENCODING="UTF-8"
#convert
CONVERT=" iconv -f $FROM_ENCODING -t $TO_ENCODING"
#loop to convert multiple files 
for  file  in  *.txt; do
$CONVERT   "$file"   -o  "${file%.jpg}.utf8.converted"
done
exit 0
