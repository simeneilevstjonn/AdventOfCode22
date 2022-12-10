x=1;c=0
$<.map{|y|a,b=y.split;print (c%40-x)**2<2 ? ?# : ?.;c+=1;(print (c%40-x)**2<2 ? ?# : ?.;c+=1;x+=b.to_i) if a<?b}