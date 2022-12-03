#!/usr/bin/j
load '../util.ijs'
half =: {{ (u~-:@#)~ }}
both =: (--:#)half<\
both =: (~.@{. half) (e.#[) (}. half)
prio =: 38-~-&58^:(>:&97)
ans +/prio"0(,both;._2 a.i.in)
NB. TODO: part 2
NB. exit''
