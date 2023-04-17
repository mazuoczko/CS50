a = input("Expression: ")
x, y, z, = a.split(" ")
n1 = int(x)
n2 = int(z)
if y == '+' :
   c = n1 + n2
   v = float(c)
   print( "%.1f" % v)
elif y == '-' :
   d = n1 - n2
   b = float(d)
   print("%.1f" % b)

elif y == '/' :
   f = n1 / n2
   b = float("%.1f" % f)
   print(b)
elif y == '*' :
   g = n1 * n2
   b = float("%.1f" % g)
   print(b)