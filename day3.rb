p$<.each_slice(3).sum{|x|(x.map(&:bytes).inject(:&)[0]+20)%58}