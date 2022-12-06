a=gets
(13...a.size).map{|i|puts i+1 if a[i-13..i].chars.uniq.size>13}