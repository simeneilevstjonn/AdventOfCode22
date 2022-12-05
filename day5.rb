a,b=`cat`.split("

")
q=a.lines.map{|y|y.scan(/\w|    /)}.reverse.transpose.map{|y|y.filter{|x|/ /!~x}}
b.scan(/\d+/).map(&:to_i).each_slice(3){|a,b,c|q[c-1]+=q[b-1].pop a}
p q.sum("",&:last)