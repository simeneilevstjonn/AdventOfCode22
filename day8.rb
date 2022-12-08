g=$<.map{|x|x.chomp.bytes}
p (0...g.size).map{|i|(0...g[0].size).map{|j|s=[g[i][0...j].reverse,g[i][j+1..-1],g[0...i].map{|x|x[j]}.reverse,g[i+1..-1].map{|x|x[j]}];s.filter(&:empty?).any? ? 0:s.map{|x|k=0;(0...x.size).map{|c|k=c;break if x[k]>=g[i][j]};k+(k==x.size ? 0:1)}.inject(:*)}.max}.max
