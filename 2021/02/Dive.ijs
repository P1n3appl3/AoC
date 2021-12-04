#!/usr/bin/j
load '../util.ijs'
in =:(;:;._2)in
d =: {."1>{."1 in
num =: ".>{:"1 in
depth =: num*(-1*d='u')+d='d'
dist =: num*d='f'
ans (+/dist)*+/depth
ans (+/dist)*+/dist*+/\depth
exit 0
