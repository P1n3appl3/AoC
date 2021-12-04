#!/usr/bin/j
load '../util.ijs'
in =: '1'&=;._2 in
g =: (#in)<+:+/in
ans (#.g)*#.-.g
p =: {{y=(#y)u+:+/y}}
reduce =: {{
a =. y
for_i. i. {:$y do.
    a =. (u p i{"1 a)#a
    if. 1=#a do. {.a return. end.
end.
}}

ans (#.>reduce in)*#.<:reduce in
exit''
