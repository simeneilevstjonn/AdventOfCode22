p STDIN.each_slice(3).map{|x|(x.map(&:bytes).inject(:&)[0]+20)%58}.sum