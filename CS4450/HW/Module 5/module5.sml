
(* Exercise 3 *)
datatype number = INT of int | REAL of real;

(* Exercise 4 *)
fun plus (INT i1) (INT i2) = INT (i1 + i2)
  | plus (INT i) (REAL r) = REAL (real i + r)
  | plus (REAL r) (INT i) = REAL (r + real i)
  | plus (REAL r1) (REAL r2) = REAL (r1 + r2);

(* Exercise 5 *)
datatype intnest = INT of int | LIST of intnest list;

fun addup (INT i) = i
  | addup (LIST nil) =  0
  | addup (LIST lyst) = addup (hd lyst) + addup (LIST (tl lyst));

(* Exercise 9 *)
datatype 'data tree = 
    Empty | 
    Node of 'data tree * 'data * 'data tree;

fun appendall Empty = nil
  | appendall (Node (l, m, r)) = appendall(l) @ m @ appendall(r);

(* Exercise 10 *)
fun isComplete Empty = true
  | isComplete (Node (Empty, _, Empty)) = true
  | isComplete (Node (Node (_, _, _), _, Node (_, _, _))) = true
  | isComplete _ = false;