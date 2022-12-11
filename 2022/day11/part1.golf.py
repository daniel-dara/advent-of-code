M={}
for i,S in enumerate(open('input.txt').read().split('\n\n')):
	L=S.split('\n')
	M[i]=[[*map(int,L[1].split(':')[1].split(','))],lambda o,f=L[2].split('=')[1]:eval(f.replace('old',str(o))),lambda w,x=[int(l.split()[-1])for l in L[3:6]]:x[2]if w%x[0]else x[1],0]
for _ in range(20):
	for m in M.values():
		while m[0]:
			M[m[2](w:=m[1](m[0].pop(0))//3)][0]+=[w]
			m[3]+=1
t=sorted(M[k][3]for k in M)[-2:]
print(t[-1]*t[-2] == 55930)
