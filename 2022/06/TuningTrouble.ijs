#!/usr/bin/env jconsole
load '../util.ijs'

solve =: {{ m+ 1 i.~m(m=[:#~.)\ y }}
ans 4 solve in
ans 14 solve in

exit''
