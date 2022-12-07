t,p,d={},[],[]
$<.map{|x|x[0,4]=="$ cd"?(a=x[5...-1];a=="/"?p=[]:(a==".."?p.pop : p+=[a])):((a=t;p.map{|y|a=a[y]};b,c=x.split;a[c]=b=="dir"?{}: b.to_i)if x!="$ ls\n")}
f=->(m){t=0;m.each{|k,a|t+=a if a.is_a? Integer;t+=f.call(a)if !a.is_a? Integer};d+=[t];t}
s=f.call(t)-4e7
p d.filter{|x|x>=s}.min