#!/usr/bin/j
load '../util.ijs'
NB. in =: 1!:1<'test'
in =: ".;._1',',}:in
sum =: {{2%~y*y+1}}
cost =: {{+/u|y-in}}
ans <./]cost"0 i.>./in
ans >.<./sum cost"0 i.>./in
