p $<.map{|x|a,b,c,d=x.scan(/\d+/).map(&:to_i);(a>d||c>b)?0:1}.sum