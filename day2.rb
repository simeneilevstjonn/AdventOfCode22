# Tie is + 0 mod 3
# Loss is + 2 mod 3
# Win is + 1 mod 3
# Rock: 1, paper: 2, scissors: 3
p STDIN.each_line.map(&:bytes).map{|a,_,b|3*b-263+(a+b-1)%3}.sum