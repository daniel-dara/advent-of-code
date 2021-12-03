h,l=(int(''.join(b),2)for b in zip(*(('1','0')[::1-2*(r.count('1')>len(r)/2)]for r in zip(*open('i').read().split()))))
print(h*l)