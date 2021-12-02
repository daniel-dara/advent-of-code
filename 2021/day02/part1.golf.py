A=sum(({'f':1j,'d':1,'u':-1}[A[0]]*int(A[-2])for A in open('input.txt')))
print(A.real*A.imag)
