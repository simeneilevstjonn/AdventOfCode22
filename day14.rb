d=$<.map{|x|x.split("->").map{|y|y.split(",").map(&:to_i)}}
g=d.map{|x|x.map{|a,b|b}}.flatten.max+2
m=(0..g).map{|i|[i==g]*(510+2*g)}
d.map{|l|(1...l.size).map{|i|x,y=l[i-1];a,b=l[i];c,d=[y,b].sort;(c..d).map{|j|m[j][x]=1};c,d=[x,a].sort;(c..d).map{|j|m[y][j]=1}}}
s=->(x,y){b=y+1;a=m[b];!a[x]?s.(x,b):!a[x-1]?s.(x-1,b):!a[x+1]?s.(x+1,b): m[y][x]=true;1}
i=0
(i+=s.(500,0))while !m[0][500]
p i