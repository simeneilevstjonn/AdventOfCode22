x=[1]
$<.map{|y|a,b=y.split;x+=[x[-1]];x+=[x[-1]+b.to_i]if a<?b}
p (0..5).map{|i|x[19+40*i]*(20+40*i)}.sum