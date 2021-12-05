#!/usr/bin/j
load '../util.ijs'
lines =: [;._2 in
wrap =: {{1+100|_1+y}}
draw =: wrap".;._1',',{.lines
board =: wrap>".each cut"1;._1}.lines
cond =: {{+./"1-.0 e.("1)2=/\"1 y}}"2
diag =: {{cond (<0 1)|: y}}
won =: {{(diag y)+.(diag|."2 y)+.(cond y)+.(cond|:"2 y)}}
remove =: {{x*-.x e.y }}
l =: #board
state =: ((l*#draw), 5 5)$,(board&remove)\draw
win =: {{(+/100|,y{state)*draw{~<.y%l}}
ans win 1 i.~won state
ans win l + 0 i:~won state
exit''
