a,b=`cat`.split("

")
q=a.scan(/[A-Z]| {4}/).each_slice(a[-2].to_i).to_a.transpose.map{|y|y.filter{|x|x.size<2}}.map(&:reverse)
b.scan(/\d+/).map(&:to_i).each_slice(3){|a,b,c|q[c-1]+=q[b-1].pop a}
p q.sum("",&:last)