t={};p=[]
for x in $<.each_line do
    if x.include?"$ cd"
        a = x.delete_prefix("$ cd ").chomp
        if a=="/"
            p = []
        elsif a==".."
            p.pop
        else
            p+=[a]
        end
    elsif x!="$ ls\n"
        a = t
        p.map{|y|a=a[y]}
        b,c=x.split
        a[c]=b=="dir"?{}: b.to_i
    end
end
def dfs(m,d)
    t = 0
    m.each{|k,a|t+=a if a.is_a? Integer;t+=dfs(a,d)unless a.is_a? Integer}
    if t <=100000
        d.append(t)
    end
    return t
end
d=[]
dfs(t,d)
p d.sum