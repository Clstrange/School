(* Exercise 2 *)
fun member (e,nil) = false
|   member (e,L) = if e = hd L then true else member(e,tl L);

(* Exercise 3 *)
fun less (e,nil) = [] 
|   less (e,L) = if hd L < e then hd L :: less (e,tl L) else less (e, tl L);

(* Exercise 4 *)
fun repeats ([a]) = false
|   repeats (L) = if hd L = hd (tl L) then true else repeats(tl L); 

(* Exercise 5 *)
fun eval ([a]:real list, x) = a
|   eval (poly,x) = (hd poly) + x * eval(tl poly, x);

(* Exercise 7 *)
fun comp (x,y) = if x < y then true else false;

fun quicksort (nil,comp) = nil
|   quicksort (pivot :: rest, comp) =
        let
          fun split(nil) = (nil,nil)
          |   split(x::xs) = 
                let
                  val (below,above) = split(xs)
                in
                  if comp(x, pivot) then (x :: below, above)
                  else (below, x :: above)
                end;
          val (below, above) = split(rest)
        in
          quicksort (below,comp) @ [pivot] @ quicksort (above,comp)
        end;


fun g stuff =
let
    fun f (nil,y) = [y]
    | f (x::rest,y) = f (rest,y) @ f (rest,x::y)
in
    f (stuff,nil)
end;

(* Exercise B *)
fun p x = x+1;

fun f2n(f,0,x) = x
|   f2n (f,n,x) = f2n(f, n-1, x) + f2n(f,0,x);