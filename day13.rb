e,f=[[2]],[[6]]
c=->(a,b){(0...[a.size,b.size].min).map{|i|m,n=a[i],b[i];g,h=[m,n].map{|x|x.class==Integer};(return -1 if m<n;return 1 if m>n;next)if g&&h;a[i]=[m]if g;b[i]=[n]if h;q=c.(a[i],b[i]);return q if q!=0};return b.size==a.size ? 0: b.size>a.size ? -1:1}
l=($<.map{|x|eval x}.compact+[e,f]).sort{|a,b|c.(a,b)}
p (1+l.index(e))*(1+l.index(f))