t,p,d={},[],[]
$<.map{|x|x[0,3]=="$ c"?(a=x[5...-1];a<"."?p=[]:(a<"0"?p.pop : p+=[a])):((a=t;p.map{|y|a=a[y]};b,c=x.split;a[c]=b>"a"?{}: b.to_i)if x>"$")}
f=->(m){t=0;m.map{|k,a|(a.is_a? Hash)?t+=f.(a): t+=a};d+=[t];t}
s=f.(t)-4e7
p d.filter{|x|x>=s}.min