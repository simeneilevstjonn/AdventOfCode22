g=$<.map(&:bytes)
c=[]
for i in 0...g.size
    for j in 0...g[0].size
        s=[0,0,0,0]
        x = g[i][0...j].reverse
        if x.size == 1
            s[0] = 1
        end
        for k in 1...x.size
            if x[k] > x[k-1]
                s[0] += 1
            
            else
                break
            end
        end    
        x=g[i][j+1..-1]
        if x.size == 1
            s[1] = 1
        end
        for k in 1...x.size
            if x[k] > x[k-1]
                s[1] += 1
            else
                break
            end
        end   
        x = g[0...i].map{|x|x[j]}.reverse
        if x.size == 1
            s[2] = 1
        end
        for k in 1...x.size
            if x[k] > x[k-1]
                s[2] += 1
            else
                break
            end
        end 
        x=g[i+1..-1].map{|x|x[j]}
        if x.size == 1
            s[3] = 1
        end
        for k in 1...x.size
            if x[k] > x[k-1]
                s[3] += 1
            else
                break
            end
        end 
        c+=[s.inject(:*)]
    end
end
p c.max