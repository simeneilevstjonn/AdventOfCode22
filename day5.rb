a,b=gets(nil).split("

");
c=a.chomp[-2].to_i
q=[[]]*c
a.scan(/[A-Z]|\s{4}/).each_slice(c){|y|y.map.with_index{|x,i|q[i]=[x]+q[i]if x.size<2}}
b.scan(/\d+/).map(&:to_i).each_slice(3).map{|a,b,c|q[c-1]+=q[b-1].pop(a)}
p q.map{|x|x[-1]}.join