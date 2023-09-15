(* Problem 3 *)
fun fourth a =
  hd (tl (tl ((tl a))));

(* Problem 4 *)
fun min3(a,b,c) =
  if a > b then min3 (b,a,c) else if b > c then min3 (a,c,b) else a;

(* Problem 5 *)
fun red(a,b,c) =
  (a,c);

(* Problem 6 *)
fun thirds a =
  hd(tl((tl (explode a ))));

(* Problem 7 *)
fun cycle1 a =
  (tl a)@[(hd a)];

(* Problem 8 *)
fun sort3(a:real,b,c) =
  if a > b then sort3 (b,a,c) else if b > c then sort3 (a,c,b) else (a,b,c);

(* Problem 9 *)
fun del3 a =
  [hd a] @ [hd(tl a)] @ tl(tl(tl(a)));

(* Problem 10 *)
fun sqsum a =
  if a > 0 then a*a + sqsum(a-1) else 0;

(* Problem 11 *)
fun cycle(a,n) = 
  if n > 0 then cycle((tl a) @ [hd a],n-1) else a;

(* Problem 13 *)
fun maxhelper(max, lyst) = 
  if null lyst
  then max 
  else if max > hd lyst
  then maxhelper(max, tl lyst)
  else maxhelper(hd lyst, tl lyst)

fun max(lyst) =
  maxhelper(hd lyst, tl lyst)

(* Problem 14 *)
fun isPrimeHelper(num, i) =
  if num = 1 orelse num = 2 then true else 
  if (i * i) > num then true else 
  if num mod i = 0 then false else 
  isPrimeHelper(num, i+1)

fun isPrime(num) =
  isPrimeHelper(num, 2)
  
(* Problem 15 *)
fun select(lyst, f) =
  if null lyst then [] else
  if f(hd lyst) = true then hd lyst :: select(tl lyst, f) else
  select(tl lyst, f)