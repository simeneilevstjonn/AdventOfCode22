p STDIN.each_line.map{|x|a,b,c,d=x.scan(/\d+/).map(&:to_i);(a<=d&&c<=b)?1:0}.sum