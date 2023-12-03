#!/usr/bin/env jconsole
load '../util.ijs'
data =: ".rplc&('-';'j');._2 in
seqs =: {{ +/>u each ([}.[:i.1+])/"1 each <"1 2+. y }}
ans (0=[:+/-./) seqs ~.data,|."1 data
ans (+./@e./) seqs data
exit''
