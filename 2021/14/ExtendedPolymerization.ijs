#!/usr/bin/env jconsole
load '../util.ijs'
in =: fread < 'test'
in =: <;._2 in
start =: >{. in
rest =: 2 }. in
from =: 2{."1 >rest
to =: {:"1 >rest
{{ 0 2 { y ,. 2 1 { y }}
