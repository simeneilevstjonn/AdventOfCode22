g=$<.map(&:bytes)
h=g.size
w=g[0].size
e=nil
s=[]
(0...h).map{|y|(0...w).map{|x|(s.append [y,x];g[y][x]=97)if (g[y][x]==83||g[y][x]==97);(e=[y,x];g[y][x]=122)if g[y][x]==69}}
p s.map{|y,x|
    d=[[1e9]*w]*h
    d[y][x]=0
    v=[[0]*w]*h
    q=Queue.new
    q.push([y,x])
    (y,x=q.pop;(v[y][x]=1;((y!=0?[[y-1,x]]:[])+(y!=h-1?[[y+1,x]]:[])+(x!=0?[[y,x-1]]:[])+(x!=w-1?[[y,x+1]]:[])).map{|a,b|(d[a][b]=1+d[y][x];q.push([a,b]))if g[a][b]-1<=g[y][y]})if v[y][x]<1)while !q.empty?
    d[e[0]][e[1]]
}.min
