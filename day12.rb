g=$<.map(&:bytes)
h=g.size
w=g[0].size
e=nil
s=[]
(0...h).map{|y|(0...w).map{|x|(s.append [y,x];g[y][x]=97)if g[y][x]==83;(e=[y,x],g[y][x]=122)if g[y][x]=69}}
p s.map{|x,y|
    d=[[1e9]*w]*h
    v=[[0]*w]*h
    q=Queue.new
    q.push(s)
    (x,y=q.pop;(((y!=0?[[y-1,x]]:[])+(y!=h-1?[[y+1,x]]:[])+(x!=0?[[y,x-1]]:[])+(x!=w-1?[[y,x+1]]:[])).map{|a,b|
        (d[a][b]=1+d[y][x];q.push([a,b]))if g[a][b]-1<=g[y][y]})if !v[y][x])while !q.empty?
    d[e[0]][e[1]]
}.min