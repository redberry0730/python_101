class a():
  pass
class b(a):
  pass
class c(b):
  pass
class d(c):
  pass
class e(d):
  pass

aa = a()
bb = b()
cc = c()
dd = d()
ee = e()


print('isinstance(bb, a) :',isinstance(bb, a))
print('isinstance(cc, b) :',isinstance(cc, b))
print('isinstance(dd, c) :',isinstance(dd, c))
print('isinstance(ee, d) :',isinstance(ee, d))

print('isinstance(cc, a) :',isinstance(cc, a))
print('isinstance(dd, b) :',isinstance(dd, b))
print('isinstance(ee, c) :',isinstance(ee, c))

print('isinstance(dd, c) :',isinstance(dd, c))
print('isinstance(ee, a) :',isinstance(ee, a))

print("---------------------------------------")

print('isinstance(aa, b) :',isinstance(aa, b))
print('isinstance(bb, c) :',isinstance(bb, c))

print("---------------------------------------")

print('isinstance(aa, c) :',isinstance(aa, c))
print('isinstance(bb, e) :',isinstance(bb, e))