r=(0..9).map{[0,0]};h=r[0]
p $<.map{|a|d,b=a.split;(1..b.to_i).map{
    h[0]+=d==?U ? 1: d==?D ? -1:0;
    h[1]+=d==?R ? 1: d==?L ? -1:0;
    (1..9).map{|i|
        t=r[i]
        f=r[i-1]
        y,x=t
        c,e=f
        if (y-c)**2+(x-e)**2>2
            t[0] += c>y ? 1: y>c ? -1:0
            t[1] += e>x ? 1: x>e ? -1:0
        end
        r[9].dup
    }
}}.uniq.size