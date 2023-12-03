#!/usr/bin/env jconsole
load '../util.ijs'
in =: 1!:1<'test'
grid =: "."0;._2 in
grid =: 4 4 $ 4 # i. 4
pad =: 0,0,~0,.0,.~]
filter =: 3 3 $ 0 1 0  1 0 1  0 1 0
NB. <;.3 pad grid
