#!/usr/bin/j
load '../util.ijs'
NB. in =: 1!:1<'test'
in =: ".;._1',',}:in
sum =: {{y*(y+1)%2}}
cost =: {{+/u|y-in}}
ans <./ ]cost"0 i.>./in
ans >. <./ sum cost"0 i.>./in
