#!/usr/bin/j
load '../util.ijs'
NB. in =: fread < 'small'
parse =: ".@rplc & ('-';'j')
seq =: 0,[}.[:i.1+]
dostuff =: {{ u seq/"1 +. parse y }}
ans +/ > {{0=#-./y +. 0=#-.~/y}} dostuff each LF cut in
ans +/ > {{ +./ e./ (}."1 y)}} dostuff each LF cut in
exit''
