print((sum(dict(f=1j,d=1,u=-1)[l[0]]*int(l[-2])for l in open('i'))**2).imag/2)
