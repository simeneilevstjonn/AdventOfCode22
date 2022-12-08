g=$<.map{|x|x.chomp.bytes}
c=[]
for i in 0...g.size
    for j in 0...g[0].size
        s = [g[i][0...j].reverse, g[i][j+1..-1], g[0...i].map{|x|x[j]}.reverse, g[i+1..-1].map{|x|x[j]}]
        a=1
        next if s.filter(&:empty?).any?
        for x in s
            k = 0
            while k < x.size and x[k] < g[i][j]
                k+=1
            end
            a*=k + (k==x.size ? 0:1)
        end
        c+=[a]
    end
end
p c.max