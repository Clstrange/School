(* Exercise 5 *)
fun inclist (lyst, i) = map (fn x=>x+1) lyst;

(* Exercise 9 *)
fun bxor lyst = foldl (fn (x,c)=> if (c andalso x) = false then true else false) false lyst;

(* Exercise 10 *)
fun duplist lyst = foldl (fn (x,c) => c@[x]@[x]) [] lyst;

(* Exercise 14 *)
fun maxpairs (lyst:(int*int) list) = 
    map (fn x => if (#1 x) > (#2 x) then (#1 x) else (#2 x)) lyst;

(* Exercise 19 *)
fun member (element, lyst) = 
    foldl (fn (x,c) => x orelse c) false 
    (map (fn x => if x = element then true else false) lyst);

(* Exercise 22 *)
fun evens (lyst) = 
    foldr (fn (x,c) => if x mod 2 = 0 then x::c else c) nil lyst;