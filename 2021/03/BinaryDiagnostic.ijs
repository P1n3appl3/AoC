#!/usr/bin/j
load '../util.ijs'
in =: '1'&=;._2 in
ans (#.*#.@:-.)(#in)<+:+/in
f =: {{ a=.y
for_i.i. {:$y do.
a=.a#~(]=#u[:+:+/)i{"1 a
if.1=#a do.{.a return.end.end.}}
ans (#.>f in)*#.<:f in
exit''
