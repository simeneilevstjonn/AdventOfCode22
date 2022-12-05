a,b=`cat`.split("

")
q=a.lines.map{|y|y.scan(/.{1,4}/).map{|x|x[1]}}.reverse.transpose.map{|y|y.filter{|x|x.ord>32}}
b.scan(/\d+/).map(&:to_i).each_slice(3){|a,b,c|q[c-1]+=q[b-1].pop a}
p q.sum("",&:last)