r=(0..9).map{[0,0]}
v=[]
$<.map{|x|d,b=x.split
    (1..b.to_i).map{ |j|
        if d== ?U
            r[0][0]+=1
        elsif d== ?D
            r[0][0]-=1
        elsif d== ?L
            r[0][1]-=1
        elsif d== ?R
            r[0][1]+=1
        end

        (1..9).map{|i|
            if (r[i][0] - r[i - 1][0])**2 + (r[i][1] - r[i - 1][1])**2 > 2
                r[i][0] += ((r[i - 1][0] > r[i][0])?1:0) - ((r[i - 1][0] < r[i][0])?1:0)
                r[i][1] += ((r[i - 1][1] > r[i][1])?1:0) - ((r[i - 1][1] < r[i][1])?1:0)
            end
            v.append [r[9][0], r[9][1]]
        }
    }
}
p v.uniq.size