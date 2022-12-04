#!/usr/bin/j
load '../util.ijs'
both =: {{ (e.#[)/(--:#y)~.\y }}
prio =: 38-~-&58^:(>:&97)"0@(a.&i.)
ans +/prio({."1 both;._2 in)
union =: ~.@([-.-.)/@:>
ans +/prio,_3 union\(<;._2 in)
exit''
