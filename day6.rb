a=gets
s=a.size
(3...a.size).map{|i|puts i+1 if a[i-3..i].chars.uniq.size>3}