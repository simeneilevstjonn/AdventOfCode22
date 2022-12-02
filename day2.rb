# Tie is + 0 mod 3
# Loss is + 2 mod 3
# Win is + 1 mod 3
# Rock: 1, paper: 2, scissors: 3
p gets(nil).split(/$/).map{|x|x.split.map(&:ord)}.map{|a,b|3*(b-88)+1+(a+b-1)%3}.sum