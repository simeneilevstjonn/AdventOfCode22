a=gets
p (13...a.size).filter_map{|i|i+1 if a[i-13..i].chars.uniq.size>13}[0]