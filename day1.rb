#p File.read("data1.txt").split("\n\n").map{|i|i.split("\n").map(&:to_i).sum}.sort[-3,3].sum
p gets(nil).split(/\n$/).map{|i|i.split.map(&:to_i).sum}.max(3).sum