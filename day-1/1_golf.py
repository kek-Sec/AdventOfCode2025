p,c=50,0
for r in open("input.txt").read().split():p=(p+int(r[1:])*(1,-1)[r<'R'])%100;c+=p<1
print(c)
