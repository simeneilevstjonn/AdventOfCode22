g=$<.map(&:bytes)
h=g.size
w=g[0].size
e,f=0,0
s=[]
(0...h).map{|y|(0...w).map{|x|(s.append [y,x];g[y][x]=97)if (g[y][x]==83||g[y][x]==97);(e,f=y,x;g[y][x]=122)if g[y][x]==69}}
p s.map{|o,p|d=(1..h).map{[1e9]*w};d[o][p]=0;v=(1..h).map{[0]*w};q=Queue.new;q.push [o,p];(y,x=q.pop;(v[y][x]=1;((y!=0?[[y-1,x]]:[])+(y!=h-1?[[y+1,x]]:[])+(x!=0?[[y,x-1]]:[])+(x!=w-1?[[y,x+1]]:[])).map{|a,b|(d[a][b]=1+d[y][x];q.push([a,b]))if g[a][b]-2<g[y][x]})if v[y][x]<1)while !q.empty?;d[e][f]}.min