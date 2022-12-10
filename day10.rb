x=1;c=0
r=->{print (c%40-x)**2<2??#:?.;c+=1;print "\n"if c%40==0}
$<.map{|y|a,b=y.split;r.();(r.();x+=b.to_i) if a<?b}