r=(0..9).map{[0,0]}
v=[]
$<.map{|x|d,b=x.split;(1..b.to_i).map{r[0][0]+=d==?U?1:d==?D?-1:0;r[0][1]+=d==?R?1:d==?L?-1:0;(1..9).map{|i|e=r[i];f,g=r[i-1];h,l=e;(e[0]+=f>h ?1:((f<h)?-1:0);e[1]+=g>l ?1:((g<l)?-1:0))if(h-f)**2+(l-g)**2>2;v.append r[9][0,2]}}}
p v.uniq.size