g=$<.map(&:bytes)
c=0
for i in 0...g.size
    for j in 0...g[0].size
        h = g[i][j]
        # Slice on top
        if ((g[i][0...j].max||10) < h)
            c+=1
        # Slice below
        elsif ((g[i][j+1..-1].max||10) < h)
            c+=1
        # Slice on left
        elsif ((g[0...i].map{|x|x[j]}.max||10) < h)
            c+=1
        # Slice of right
        elsif ((g[i+1..-1].map{|x|x[j]}.max||10) < h)
            c+=1
        end
    end
end
p c