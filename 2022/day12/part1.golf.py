f=open(0)
w=len(f.readline())-1
m={(i//w,i%w):ord(c)for i,c in enumerate(f.read().replace('\n',''))}
s={m[k]:k for k in m if m[k] in (83,69)}
m[S:=s[83]]=97
m[E:=s[69]]=122
q=[(S,0)]
p={}
while q:
	c,t=q.pop()
	if c not in p or t<p[c]:
		p[c]=t
		q+=[(C,t+1)for C in map(lambda x:(c[0]+x[0],c[1]+x[1]),[(1,0),(-1,0),(0,1),(0,-1)])if C in m and m[C]-m[c]<= 1]
print(p[E])

