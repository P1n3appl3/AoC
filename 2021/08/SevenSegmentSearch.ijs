#!/usr/bin/j
load '../util.ijs'
NB. There's only 5040 permutations of length 7 for 7 items
in =: 1!:1<'test'
in =: {{<;._1'|',y}};._2 in
r =: {{<;._2 > {. y}}
signal =: r"1 in

