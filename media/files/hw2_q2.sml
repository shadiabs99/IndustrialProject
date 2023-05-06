fun curry(f:'a*'b -> 'c) =fn a=>fn b=>f(a,b);
fun uncurry (f:'a -> 'b -> 'c)=fn (a,b )=> f(a)(b);