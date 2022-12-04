l=STDIN.each_line.map{|x|a,b,c,d=x.split(/[\,,-]/).map(&:to_i);(a..b).to_a+(c..d).to_a}
p l.map{|x|l.map{|y|((x&y).any?)?1:0}.sum}.sum-1000