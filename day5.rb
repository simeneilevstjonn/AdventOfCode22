a,b=`cat`.split("

")
q=a.lines.map{|y|y.chars.each_slice(4).to_a}.reverse.transpose.map{|y|y.filter_map{|x|x[1]if x[1].ord>32}}
b.scan(/\d+/).map(&:to_i).each_slice(3){|a,b,c|q[c-1]+=q[b-1].pop a}
p q.sum("",&:last)