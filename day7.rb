t,p,d={},[],[]
$<.map{|x|u,v,w=x.split;w!=nil ?(w<?.?p=[]:(w<?0?p.pop : p+=[w])):((a=t;p.map{|y|a=a[y]};a[v]=u>?a?{}: u.to_i)if"$"<x)}
f=->(m){t=0;m.map{|k,a|t+=(a.is_a? Hash)?f.(a):a};d+=[t];t}
s=f.(t)-4e7
p d.filter{|x|x>=s}.min