#!/usr/bin/j
load '../util.ijs'
b =: 2+a=:4*i.(#in)%4
f =: {{(a.i.y{in)-a.i.x}}
them =: 'A'f a
me =: 'X'f b
vs =: {{+/(3*x=y)+(6*x=3|>:y)+>:x}}
ans me vs them
ans them vs~3|them+2+me
exit''
