e,f=[[2]],[[6]]
c=->(a,b){
    (0...[a.size,b.size].min).map{|i|
        g,h=[a[i],b[i]].map{|x|x.class==Integer}
        (return -1 if a[i]<b[i];return 1 if a[i]>b[i];next)if g&&h;
        a[i]=[a[i]]if g;
        b[i]=[b[i]]if h;
        q=c.(a[i],b[i]);
        return q if q!=0
    };
    return b.size==a.size ? 0: b.size>a.size ? -1:1
}
l=($<.map{|x|eval x}.filter{|x|x}+[e,f]).sort{|a,b|c.(a,b)}
p (1+l.index(e))*(1+l.index(f))