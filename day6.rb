a=gets
i=13
while a[i-13..i].chars.uniq.size<14 do
i+=1
end
puts 1+i