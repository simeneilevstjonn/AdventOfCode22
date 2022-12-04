p`cat`.split("

").map{|i|i.split.sum(&:to_i)}.max(3).sum