a,b=gets(nil).split("

");
c=a.chomp[-2].to_i
q=[[]]*c
a.scan(/[A-Z]|\s{4}/).each_slice(c).map.with_index{|x,i|q[i]=[x]+q[i]}
p q
b.scan(/\d+/).map(&:to_i).each_slice(3).map{|a,b,c|(1..a).map{q[c-1]+=[q[b-1].pop]}}
p q.join{|x|x[-1]}