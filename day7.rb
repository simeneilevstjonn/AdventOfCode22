t,p,d={},[],[]
$<.map{|x|x[2]=="c"?(a=x[5..-2];a<"."?p=[]:(a<"0"?p.pop : p+=[a])):((a=t;p.map{|y|a=a[y]};b,c=x.split;a[c]=b>"a"?{}: b.to_i)if x>"$")}
f=->(m){t=0;m.map{|k,a|t+=(a.is_a? Hash)?f.(a):a};d+=[t];t}
s=f.(t)-4e7
p d.filter{|x|x>=s}.min