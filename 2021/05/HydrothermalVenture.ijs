#!/usr/bin/env jconsole
load '../util.ijs'
in =: 1!:1<'test'
nums =: >".each'[[:digit:]]+'rxall in
lines =: _2[\_2 j./\nums

NB. ans 'blah'
NB. exit''
