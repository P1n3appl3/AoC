#!/usr/bin/j
load '../util.ijs'
both =: {{ (e.#[)/(--:#y)[\y }}
prio =: 38-~-&58^:(>:&97)
ans +/prio"0({."1 both;._2 a.i.in)
union =: {{ ~.([-.-.)/>y }}
ans +/prio"0 a.i.,_3 union\(<;._2 in)
exit''
