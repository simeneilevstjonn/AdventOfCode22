q=[];f=[];t=[];m=[];o=[]
gets(nil).split("\n\n").map{|x|_,b,c,d,e,a=x.split("\n");q+=[b.scan(/\d+/).map(&:to_i)];o+=[c[19..]];m+=[d[21..].to_i];t+=[e[29..].to_i];f+=[a[30..].to_i]}
c=f.size
p=[0]*c
(0..1e5).map{(0...c).map{|i|q[i].map{|x|y,z=o[i].gsub("old",x.to_s).scan(/\d+/).map(&:to_i);x=(o[i]=~/\*/? y*z : y+z)%m.inject(:*);x%m[i]<1?(q[t[i]].append x):(q[f[i]].append x);p[i]+=1}}}
p.sort!
p p[-1] * p[-2]