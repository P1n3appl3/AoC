#!/usr/bin/j
load '../util.ijs'

lines =: <;._2 in
gap =: a:i.~lines
art =: >gap take lines
cols =: >:4*i.4%~>:#>{: art
stacks =: |.@deb each <"1 |: }: cols {"1 art
original =: stacks
steps =: >a:-.~"1".each ;:>lines drop~>:gap

move =: {{ NB. smoutput 'moving ',(":m),' from ',(":x),' to ',":y
  'tmp new' =. (-m)split x pick stacks
  stacks =: stacks x}~ <new
  stacks =: stacks y}~ <tmp,~y pick stacks
  y }}
run =: {{ 'times from to' =: y
  (<:from) 1 move ^:times <: to }}"1

run steps
ans > {: each stacks

stacks =: original
run =: {{ 'num from to' =: y
  (<:from) num move <:to }}"1

run steps
ans > {: each stacks

exit''
