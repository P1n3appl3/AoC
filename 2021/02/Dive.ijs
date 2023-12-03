#!/usr/bin/env jconsole
load '../util.ijs'
in =: ;:;._2 in
d =: {."1>{."1 in
num =: ".>{:"1 in
depths =: +/\num*(-1*d='u')+d='d'
dist =: num*d='f'
ans (+/dist)*{:depths
ans (+/dist)*+/dist*depths
exit''
