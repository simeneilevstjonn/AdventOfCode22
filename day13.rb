l=$<.map{|x|eval x}.filter{|x|x}+[[[2]],[[6]]]
c=->(a,b){
    (0...[a.size,b.size].min).map{|i|
        (a[i]<b[i]? (return -1) : (a[i]>b[i]? (return 1) : next))if a[i].class==Integer&&b[i].class==Integer;
        a[i]=[a[i]]if a[i].class==Integer;
        b[i]=[b[i]]if b[i].class==Integer;
        q=c.(a[i],b[i])
        return q if q!=0
    };
    return b.size==a.size ? 0 : (b.size > a.size ? -1 : 1)
}

l.sort{|a,b|c.(a,b)}
p (1+l.index([[2]]))*(1+l.index([[6]]))