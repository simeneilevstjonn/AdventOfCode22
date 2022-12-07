t={};p=[]
$<.map{|x|x[0,4]=="$ cd"?(a=x[5...-1];a=="/"?p=[]:(a==".."?p.pop : p+=[a])):((a=t;p.map{|y|a=a[y]};b,c=x.split;a[c]=b=="dir"?{}: b.to_i)if x!="$ ls\n")}
def dfs(m,d)
    t = 0
    m.each{|k,a|t+=a if a.is_a? Integer;t+=dfs(a,d)unless a.is_a? Integer}
    d.append(t)
    return t
end
d=[]
s=dfs(t,d)-4e7
p d.filter{|x|x>=s}.min