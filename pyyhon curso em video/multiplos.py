s = float(input('salario'))
if s <= 1250:
    n = s + (s * 15/100)
else:
    n = s + (s * 10/100)
print("ganha {:.2f} passa a ganhar {:.2f}".format(s,n))