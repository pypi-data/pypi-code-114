# G-matrix and V' terms pulled from Mathematica notebook very kindly provided by John Frederick

from Psience.AnalyticModels import sym, SymbolicCaller, AnalyticModelBase

m = SymbolicCaller(AnalyticModelBase.symbolic_m)
r = SymbolicCaller(AnalyticModelBase.symbolic_r)
a = SymbolicCaller(AnalyticModelBase.symbolic_a)
t = SymbolicCaller(AnalyticModelBase.symbolic_t)
y = SymbolicCaller(AnalyticModelBase.symbolic_y)
sin = sym.sin; cos = sym.cos; cot = sym.cot; tan = sym.tan; csc = sym.csc
L = SymbolicCaller(AnalyticModelBase.lam)

g = {
  (('r','r'),(1,2),(1,2)):1/m[1]+1/m[2],
  (('r','r'),(1,2),(1,3)):cos(a[2,1,3])*1/m[1],
  (('r','a'),(1,2),(1,2,3)):-1*1/m[2]*1/r[2,3]*sin(a[1,2,3]),
  (('r','a'),(1,2),(1,3,4)):cos(t[2,1,3,4])*1/m[1]*1/r[1,3]*sin(a[2,1,3]),
  (('r','a'),(1,2),(3,1,4)):-1*1/m[1]*sin(a[3,1,4])*(cos(a[2,1,3])*1/r[1,4]*sin(a[3,1,4])+cos(y[3,1,2,4])*sin(a[2,1,3])*L[3,1,4]),
  (('r','t'),(1,2),(1,2,3,4)):-1*cot(a[2,3,4])*1/m[2]*1/r[2,3]*sin(t[1,2,3,4])*sin(a[1,2,3]),
  (('r','t'),(1,2),(3,2,1,4)):0,
  (('r','t'),(1,2),(1,3,4,5)):-1*csc(a[1,3,4])*1/m[1]*1/r[1,3]*sin(t[2,1,3,4])*sin(a[2,1,3]),
  (('r','t'),(1,2),(3,4,1,5)):-1*1/m[1]*sin(a[2,1,4])*(cot(a[1,4,3])*1/r[1,4]*sin(t[3,4,1,2])+-1*sin(t[3,4,1,2]+-1*t[3,4,1,5])*L[5,1,4]),
  (('r','y'),(1,2),(1,2,3,4)):0,
  (('r','y'),(1,2),(3,2,1,4)):-1*1/m[2]*sin(a[1,2,3])*sin(y[3,2,1,4])*L[4,2,3],
  (('r','y'),(1,2),(1,3,4,5)):1/m[1]*1/r[1,3]*sin(a[2,1,3])*(cot(a[1,3,4])*sin(t[2,1,3,4])+-1*cot(a[1,3,5])*sin(t[2,1,3,4]+y[1,3,4,5])),
  (('r','y'),(1,2),(3,4,1,5)):csc(a[1,4,3])*1/m[1]*1/r[1,4]*sin(t[2,1,4,3])*sin(a[2,1,4]),
  (('r','y'),(1,2),(3,1,4,5)):1/m[1]*sin(a[2,1,3])*(sin(y[3,1,2,4])*L[4,1,3]+-1*sin(y[3,1,2,4]+y[3,1,4,5])*L[5,1,3]),
  (('a','a'),(1,2,3),(1,2,3)):1/r[1,2]**2*(1/m[1]+1/m[2])+1/r[2,3]**2*(1/m[2]+1/m[3])+-2*cos(a[1,2,3])*1/m[2]*1/r[1,2]*1/r[2,3],
  (('a','a'),(1,2,3),(2,1,4)):-1*cos(t[3,2,1,4])*1/r[1,2]*(1/m[2]*sin(a[1,2,3])*L[1,2,3]+1/m[1]*sin(a[2,1,4])*L[2,1,4]),
  (('a','a'),(1,2,3),(1,2,4)):cos(y[1,2,3,4])*1/m[1]*1/r[1,2]**2+1/m[2]*sin(a[1,2,3])*sin(a[1,2,4])*(1/r[2,3]*1/r[2,4]+cos(y[1,2,3,4])*L[1,2,3]*L[1,2,4]),
  (('a','a'),(1,2,3),(1,4,5)):-1*1/m[1]*1/r[1,2]*1/r[1,4]*(cos(t[2,1,4,5])*cos(t[3,2,1,4])*cos(a[2,1,4])+sin(t[2,1,4,5])*sin(t[3,2,1,4])),
  (('a','a'),(1,2,3),(4,1,5)):-1*1/m[1]*1/r[1,2]*sin(a[4,1,5])*(cos(t[3,2,1,4])*1/r[1,5]*sin(a[2,1,4])+L[4,1,5]*(-1*cos(t[3,2,1,4])*cos(a[2,1,4])*cos(y[4,1,2,5])+sin(t[3,2,1,4])*sin(y[4,1,2,5]))),
  (('a','a'),(1,2,3),(4,2,5)):1/m[2]*sin(a[1,2,3])*sin(a[4,2,5])*(cos(a[1,2,4])*1/r[2,3]*1/r[2,5]+sin(a[1,2,4])*(cos(y[1,2,3,4])*1/r[2,5]*L[1,2,3]+cos(y[4,2,1,5])*1/r[2,3]*L[4,2,5])+L[1,2,3]*L[4,2,5]*(-1*cos(a[1,2,4])*cos(y[1,2,3,4])*cos(y[4,2,1,5])+sin(y[1,2,3,4])*sin(y[4,2,1,5]))),
  (('a','t'),(1,2,3),(1,2,3,4)):1/r[2,3]*sin(t[1,2,3,4])*(cot(a[2,3,4])*1/m[2]*sin(a[1,2,3])*L[3,2,1]+-1*1/m[3]*L[4,3,2]),
  (('a','t'),(1,2,3),(2,1,4,5)):csc(a[2,1,4])*1/m[2]*1/r[1,2]*sin(t[3,2,1,4])*sin(a[1,2,3])*L[1,2,3]+1/m[1]*1/r[1,2]*(-1*cot(a[1,4,5])*1/r[1,4]*(-1*cos(t[3,2,1,4])*cos(a[2,1,4])*sin(t[2,1,4,5])+cos(t[2,1,4,5])*sin(t[3,2,1,4]))+sin(t[3,2,1,4])*L[2,1,4]),
  (('a','t'),(1,2,3),(4,2,1,5)):1/m[1]*1/r[1,2]*(cot(a[1,2,4])*1/r[1,2]*sin(t[3,2,1,5]+-1*t[4,2,1,5])+-1*sin(t[3,2,1,5])*L[5,1,2])+1/m[2]*sin(a[1,2,3])*L[1,2,3]*(cot(a[2,1,5])*1/r[1,2]*sin(t[3,2,1,5])+-1*sin(t[3,2,1,5]+-1*t[4,2,1,5])*L[4,2,1]),
  (('a','t'),(1,2,3),(1,2,4,5)):-1*csc(a[1,2,4])*1/m[1]*1/r[1,2]**2*sin(y[1,2,3,4])+1/m[2]*sin(a[1,2,3])*(-1*sin(y[1,2,3,4])*L[1,2,3]*L[1,2,4]+cot(a[2,4,5])*1/r[2,4]*(1/r[2,3]*sin(t[1,2,4,5])*sin(a[1,2,4])+L[1,2,3]*(-1*cos(a[1,2,4])*cos(y[1,2,3,4])*sin(t[1,2,4,5])+cos(t[1,2,4,5])*sin(y[1,2,3,4])))),
  (('a','t'),(1,2,3),(1,4,5,6)):-1*csc(a[1,4,5])*1/m[1]*1/r[1,2]*1/r[1,4]*(-1*cos(t[3,2,1,4])*cos(a[2,1,4])*sin(t[2,1,4,5])+cos(t[2,1,4,5])*sin(t[3,2,1,4])),
  (('a','t'),(1,2,3),(4,5,1,6)):-1*1/m[1]*1/r[1,2]*(sin(t[3,2,1,5])*(cos(t[2,1,5,4])*cot(a[1,5,4])*1/r[1,5]+-1*cos(t[2,1,5,4]+-1*t[4,5,1,6])*L[6,1,5])+-1*cos(t[3,2,1,5])*cos(a[2,1,5])*(cot(a[1,5,4])*1/r[1,5]*sin(t[2,1,5,4])+-1*sin(t[2,1,5,4]+-1*t[4,5,1,6])*L[6,1,5])),
  (('a','t'),(1,2,3),(2,4,5,6)):csc(a[2,4,5])*1/m[2]*1/r[2,4]*sin(a[1,2,3])*(1/r[2,3]*sin(t[1,2,4,5])*sin(a[1,2,4])+-1*L[1,2,3]*(cos(a[1,2,4])*cos(y[1,2,4,3])*sin(t[1,2,4,5])+cos(t[1,2,4,5])*sin(y[1,2,4,3]))),
  (('a','t'),(1,2,3),(4,5,2,6)):1/m[2]*sin(a[1,2,3])*(sin(y[1,2,5,3])*L[1,2,3]*(-1*cos(t[1,2,5,4])*cot(a[2,5,4])*1/r[2,5]+cos(t[1,2,5,4]+-1*t[4,5,2,6])*L[6,2,5])+1/r[2,3]*sin(a[1,2,5])+-1*cos(a[1,2,5])*cos(y[1,2,5,3])*L[1,2,3]*(cot(a[2,5,4])*1/r[2,5]*sin(t[1,2,5,4])+-1*sin(t[1,2,5,4]+-1*t[4,5,2,6])*L[6,2,5])),
  (('a','y'),(1,2,3),(1,2,3,4)):sin(y[1,2,3,4])*(-1*cot(a[1,2,4])*1/m[1]*1/r[1,2]**2+1/m[2]*sin(a[1,2,3])*L[1,2,3]*L[4,2,1]),
  (('a','y'),(1,2,3),(2,1,4,5)):1/r[1,2]*(sin(t[3,2,1,4])*(-1*cot(a[2,1,4])*1/m[2]*sin(a[1,2,3])*L[1,2,3]+1/m[1]*L[4,1,2])+-1*sin(t[3,2,1,4]+y[2,1,4,5])*(-1*cot(a[2,1,5])*1/m[2]*sin(a[1,2,3])*L[1,2,3]+1/m[1]*L[5,1,2])),
  (('a','y'),(1,2,3),(4,1,2,5)):-1*csc(a[2,1,4])*1/m[2]*1/r[1,2]*sin(t[3,2,1,4])*sin(a[1,2,3])*L[1,2,3]+1/m[1]*1/r[1,2]*(-1*sin(t[3,2,1,4])*L[2,1,4]+L[5,1,4]*(cos(y[4,1,2,5])*sin(t[3,2,1,4])+cos(t[3,2,1,4])*cos(a[2,1,4])*sin(y[4,1,2,5]))),
  (('a','y'),(1,2,3),(1,2,4,5)):sin(y[1,2,3,4])*(cot(a[1,2,4])*1/m[1]*1/r[1,2]**2+-1*1/m[2]*sin(a[1,2,3])*L[1,2,3]*L[4,2,1])+-1*sin(y[1,2,3,4]+y[1,2,4,5])*(cot(a[1,2,5])*1/m[1]*1/r[1,2]**2+-1*1/m[2]*sin(a[1,2,3])*L[1,2,3]*L[5,2,1]),
  (('a','y'),(1,2,3),(4,2,1,5)):csc(a[1,2,4])*1/m[1]*1/r[1,2]**2*sin(y[1,2,3,4])+1/m[2]*sin(a[1,2,3])*(1/r[2,3]*sin(a[1,2,4])*sin(y[4,2,1,5])*L[5,2,4]+L[1,2,3]*(-1*cos(a[1,2,4])*cos(y[1,2,3,4])*sin(y[4,2,1,5])*L[5,2,4]+sin(y[1,2,3,4])*(L[1,2,4]+-1*cos(y[4,2,1,5])*L[5,2,4]))),
  (('a','y'),(1,2,3),(1,4,5,6)):1/m[1]*1/r[1,2]*1/r[1,4]*(sin(t[3,2,1,4])*(cos(t[2,1,4,5])*cot(a[1,4,5])+-1*cos(t[2,1,4,5]+y[1,4,5,6])*cot(a[1,4,6]))+-1*cos(t[3,2,1,4])*cos(a[2,1,4])*(cot(a[1,4,5])*sin(t[2,1,4,5])+-1*cot(a[1,4,6])*sin(t[2,1,4,5]+y[1,4,5,6]))),
  (('a','y'),(1,2,3),(4,5,1,6)):csc(a[1,5,4])*1/m[1]*1/r[1,2]*1/r[1,5]*(-1*cos(t[3,2,1,5])*cos(a[2,1,5])*sin(t[2,1,5,4])+cos(t[2,1,5,4])*sin(t[3,2,1,5])),
  (('a','y'),(1,2,3),(4,1,5,6)):-1*1/m[1]*1/r[1,2]*(sin(t[3,2,1,4])*(cos(y[4,1,2,5])*L[5,1,4]+-1*cos(y[4,1,2,5]+y[4,1,5,6])*L[6,1,4])+cos(t[3,2,1,4])*cos(a[2,1,4])*(sin(y[4,1,2,5])*L[5,1,4]+-1*sin(y[4,1,2,5]+y[4,1,5,6])*L[6,1,4])),
  (('a','y'),(1,2,3),(2,4,5,6)):1/m[2]*1/r[2,4]*sin(a[1,2,3])*(sin(y[1,2,4,3])*L[1,2,3]*(cos(t[1,2,4,5])*cot(a[2,4,5])+-1*cos(t[1,2,4,5]+y[2,4,5,6])*cot(a[2,4,6]))+cot(a[2,4,5])*sin(t[1,2,4,5])+-1*cot(a[2,4,6])*sin(t[1,2,4,5]+y[2,4,5,6])*(-1*1/r[2,3]*sin(a[1,2,4])+cos(a[1,2,4])*cos(y[1,2,4,3])*L[1,2,3])),
  (('a','y'),(1,2,3),(4,5,2,6)):-1*csc(a[2,5,4])*1/m[2]*1/r[2,5]*sin(a[1,2,3])*(1/r[2,3]*sin(t[1,2,5,4])*sin(a[1,2,5])+-1*L[1,2,3]*(cos(a[1,2,5])*cos(y[1,2,5,3])*sin(t[1,2,5,4])+cos(t[1,2,5,4])*sin(y[1,2,5,3]))),
  (('a','y'),(1,2,3),(4,2,5,6)):1/m[2]*sin(a[1,2,3])*(-1*sin(y[1,2,4,3])*L[1,2,3]*(cos(y[4,2,1,5])*L[5,2,4]+-1*cos(y[4,2,1,5]+y[4,2,5,6])*L[6,2,4])+-1*1/r[2,3]*sin(a[1,2,4])+cos(a[1,2,4])*cos(y[1,2,4,3])*L[1,2,3]*(sin(y[4,2,1,5])*L[5,2,4]+-1*sin(y[4,2,1,5]+y[4,2,5,6])*L[6,2,4])),
  (('t','t'),(1,2,3,4),(1,2,3,4)):csc(a[1,2,3])**2*1/m[1]*1/r[1,2]**2+csc(a[2,3,4])**2*1/m[4]*1/r[3,4]**2+1/m[2]*(cot(a[2,3,4])**2*1/r[2,3]**2+L[1,2,3]**2)+-2*cos(t[1,2,3,4])*1/r[2,3]*(cot(a[2,3,4])*1/m[2]*L[1,2,3]+cot(a[1,2,3])*1/m[3]*L[4,3,2])+1/m[3]*(cot(a[1,2,3])**2*1/r[2,3]**2+L[4,3,2]**2),
  (('t','t'),(1,2,3,4),(1,2,3,5)):csc(a[1,2,3])**2*1/m[1]*1/r[1,2]**2+cot(a[1,2,3])**2*1/m[3]*1/r[2,3]**2+1/m[2]*L[1,2,3]**2+cos(t[1,2,3,4]+-1*t[1,2,3,5])*(cot(a[2,3,4])*cot(a[2,3,5])*1/m[2]*1/r[2,3]**2+1/m[3]*L[4,3,2]*L[5,3,2])+-1*1/r[2,3]*(cos(t[1,2,3,4])*(cot(a[2,3,4])*1/m[2]*L[1,2,3]+cot(a[1,2,3])*1/m[3]*L[4,3,2])+cos(t[1,2,3,5])*(cot(a[2,3,5])*1/m[2]*L[1,2,3]+cot(a[1,2,3])*1/m[3]*L[5,3,2])),
  (('t','t'),(1,2,3,4),(3,2,1,5)):csc(a[1,2,3])*1/m[3]*1/r[2,3]*(cot(a[1,2,3])*1/r[2,3]+-1*cos(t[1,2,3,4])*L[4,3,2])+csc(a[1,2,3])*1/m[1]*1/r[1,2]*(cot(a[1,2,3])*1/r[1,2]+-1*cos(t[3,2,1,5])*L[5,1,2])+1/m[2]*(-1*cot(a[2,1,5])*cot(a[2,3,4])*1/r[1,2]*1/r[2,3]*(cos(t[1,2,3,4])*cos(t[3,2,1,5])+cos(a[1,2,3])*sin(t[1,2,3,4])*sin(t[3,2,1,5]))+cos(t[3,2,1,5])*cot(a[2,1,5])*1/r[1,2]*L[1,2,3]+cos(t[1,2,3,4])*cot(a[2,3,4])*1/r[2,3]*L[3,2,1]+-1*L[1,2,3]*L[3,2,1]),
  (('t','t'),(1,2,3,4),(1,2,5,6)):cos(y[1,2,3,5])*csc(a[1,2,3])*csc(a[1,2,5])*1/m[1]*1/r[1,2]**2+1/m[2]*(-1*cot(a[2,5,6])*1/r[2,5]*L[1,2,3]*(cos(t[1,2,5,6])*cos(y[1,2,3,5])+cos(a[1,2,5])*sin(t[1,2,5,6])*sin(y[1,2,3,5]))+-1*cot(a[2,3,4])*1/r[2,3]*L[1,2,5]*(cos(t[1,2,3,4])*cos(y[1,2,3,5])+-1*cos(a[1,2,3])*sin(t[1,2,3,4])*sin(y[1,2,3,5]))+cos(y[1,2,3,5])*L[1,2,3]*L[1,2,5]+cot(a[2,3,4])*1/r[2,3]*1/r[2,5]*cot(a[2,5,6])*(cos(t[1,2,3,4])*cos(t[1,2,5,6])*cos(y[1,2,3,5])+sin(t[1,2,3,4])*sin(t[1,2,5,6])*(cos(a[1,2,3])*cos(a[1,2,5])*cos(y[1,2,3,5])+sin(a[1,2,3])*sin(a[1,2,5]))+sin(y[1,2,3,5])*(-1*cos(t[1,2,5,6])*cos(a[1,2,3])*sin(t[1,2,3,4])+cos(t[1,2,3,4])*cos(a[1,2,5])*sin(t[1,2,5,6])))),
  (('t','t'),(1,2,3,4),(5,2,1,6)):1/m[2]*(-1*cot(a[2,1,6])*cot(a[2,3,4])*1/r[1,2]*1/r[2,3]*(cos(t[1,2,3,4])*cos(t[3,2,1,6])+cos(a[1,2,3])*sin(t[1,2,3,4])*sin(t[3,2,1,6]))+cos(t[3,2,1,6])*cot(a[2,1,6])*1/r[1,2]*L[1,2,3]+cot(a[2,3,4])*1/r[2,3]*L[5,2,1]*(cos(t[1,2,3,4])*cos(t[3,2,1,6]+-1*t[5,2,1,6])+cos(a[1,2,3])*sin(t[1,2,3,4])*sin(t[3,2,1,6]+-1*t[5,2,1,6]))+-1*cos(t[3,2,1,6]+-1*t[5,2,1,6])*L[1,2,3]*L[5,2,1])+csc(a[1,2,3])*1/m[1]*1/r[1,2]*(cos(t[3,2,1,6]+-1*t[5,2,1,6])*cot(a[1,2,5])*1/r[1,2]+-1*cos(t[3,2,1,6])*L[6,1,2]),
  (('t','t'),(1,2,3,4),(2,1,5,6)):csc(a[1,2,3])*1/m[1]*1/r[1,2]*(-1*cot(a[1,5,6])*1/r[1,5]*(cos(t[2,1,5,6])*cos(t[3,2,1,5])+cos(a[2,1,5])*sin(t[2,1,5,6])*sin(t[3,2,1,5]))+cos(t[3,2,1,5])*L[2,1,5])+csc(a[2,1,5])*1/m[2]*1/r[1,2]*(-1*cot(a[2,3,4])*1/r[2,3]*(cos(t[1,2,3,4])*cos(t[3,2,1,5])+cos(a[1,2,3])*sin(t[1,2,3,4])*sin(t[3,2,1,5]))+cos(t[3,2,1,5])*L[1,2,3]),
  (('t','t'),(1,2,3,4),(5,2,3,6)):cos(t[1,2,3,6]+-1*t[5,2,3,6])*(cot(a[3,2,1])*cot(a[3,2,5])*1/m[3]*1/r[3,2]**2+1/m[2]*L[1,2,3]*L[5,2,3])+cos(t[1,2,3,4]+-1*t[1,2,3,6])*(cot(a[2,3,4])*cot(a[2,3,6])*1/m[2]*1/r[3,2]**2+1/m[3]*L[4,3,2]*L[6,3,2])+-1*1/r[3,2]*(cos(t[1,2,3,4]+-1*t[1,2,3,6]+t[5,2,3,6])*(cot(a[3,2,5])*1/m[3]*L[4,3,2]+cot(a[2,3,4])*1/m[2]*L[5,2,3])+cos(t[1,2,3,6])*(cot(a[2,3,6])*1/m[2]*L[1,2,3]+cot(a[3,2,1])*1/m[3]*L[6,3,2])),
  (('t','t'),(1,2,3,4),(1,5,6,7)):-1*csc(a[1,2,3])*csc(a[1,5,6])*1/m[1]*1/r[1,2]*1/r[1,5]*(cos(t[2,1,5,6])*cos(t[3,2,1,5])+cos(a[2,1,5])*sin(t[2,1,5,6])*sin(t[3,2,1,5])),
  (('t','t'),(1,2,3,4),(5,6,1,7)):csc(a[1,2,3])*1/m[1]*1/r[1,2]*(-1*cot(a[1,6,5])*1/r[1,6]*(cos(t[2,1,6,5])*cos(t[3,2,1,6])+cos(a[2,1,6])*sin(t[2,1,6,5])*sin(t[3,2,1,6]))+L[7,1,6]*(cos(t[3,2,1,6])*cos(t[2,1,6,5]+-1*t[5,6,1,7])+cos(a[2,1,6])*sin(t[3,2,1,6])*sin(t[2,1,6,5]+-1*t[5,6,1,7]))),
  (('t','t'),(1,2,3,4),(5,6,3,7)):1/m[3]*(-1*cos(t[1,2,3,6])*cot(a[3,2,1])*1/r[3,2]+cos(t[1,2,3,4]+-1*t[1,2,3,6])*L[4,3,2]*(cos(t[2,3,6,5])*cot(a[3,6,5])*1/r[3,6]+-1*cos(t[2,3,6,5]+-1*t[5,6,3,7])*L[7,3,6])+-1*cos(a[2,3,6])*(cot(a[3,2,1])*1/r[3,2]*sin(t[1,2,3,6])+sin(t[1,2,3,4]+-1*t[1,2,3,6])*L[4,3,2])*(cot(a[3,6,5])*1/r[3,6]*sin(t[2,3,6,5])+-1*sin(t[2,3,6,5]+-1*t[5,6,3,7])*L[7,3,6])),
  (('t','y'),(1,2,3,4),(1,2,3,5)):-1*csc(a[1,2,3])*1/m[1]*1/r[1,2]**2*(cot(a[1,2,3])+-1*cos(y[1,2,3,5])*cot(a[1,2,5]))+-1*csc(a[1,2,3])*1/m[3]*1/r[2,3]*(cot(a[1,2,3])*1/r[2,3]+-1*cos(t[1,2,3,4])*L[4,3,2])+1/m[2]*(L[3,2,1]*(-1*cos(t[1,2,3,4])*cot(a[2,3,4])*1/r[2,3]+L[1,2,3])+L[5,2,1]*(-1*cos(y[1,2,3,5])*L[1,2,3]+cot(a[2,3,4])*1/r[2,3]*(cos(t[1,2,3,4])*cos(y[1,2,3,5])+-1*cos(a[1,2,3])*sin(t[1,2,3,4])*sin(y[1,2,3,5])))),
  (('t','y'),(1,2,3,4),(3,2,1,5)):-1*csc(a[1,2,3])**2*1/m[1]*1/r[1,2]**2+1/m[2]*(cot(a[2,3,4])*1/r[2,3]*(cos(t[1,2,3,4])*L[1,2,3]+-1*cos(t[1,2,3,4]+y[3,2,1,5])*L[5,2,3])+L[1,2,3]*(-1*L[1,2,3]+cos(y[3,2,1,5])*L[5,2,3]))+1/m[3]*1/r[2,3]*(cot(a[1,2,3])*1/r[2,3]*(-1*cot(a[1,2,3])+cos(y[3,2,1,5])*cot(a[3,2,5]))+L[4,3,2]*(cos(t[1,2,3,4])*cot(a[1,2,3])+-1*cos(t[1,2,3,4]+y[3,2,1,5])*cot(a[3,2,5]))),
  (('t','y'),(1,2,3,4),(1,2,5,6)):1/m[2]*(-1*cos(t[1,2,3,4])*cot(a[2,3,4])*1/r[2,3]+L[1,2,3]*(cos(y[1,2,3,5])*L[5,2,1]+-1*cos(y[1,2,3,5]+y[1,2,5,6])*L[6,2,1])+-1*cos(a[1,2,3])*cot(a[2,3,4])*1/r[2,3]*sin(t[1,2,3,4])*(sin(y[1,2,3,5])*L[5,2,1]+-1*sin(y[1,2,3,5]+y[1,2,5,6])*L[6,2,1]))+-1*csc(a[1,2,3])*1/m[1]*1/r[1,2]**2*(cos(y[1,2,3,5])*cot(a[1,2,5])+-1*cos(y[1,2,3,5]+y[1,2,5,6])*cot(a[1,2,6])),
  (('t','y'),(1,2,3,4),(5,2,1,6)):-1*cos(y[1,2,3,5])*csc(a[1,2,3])*csc(a[1,2,5])*1/m[1]*1/r[1,2]**2+1/m[2]*(-1*cot(a[2,3,4])*1/r[2,3]*sin(t[1,2,3,4])*(-1*sin(y[5,2,1,6])*L[6,2,5]*(cos(a[1,2,3])*cos(a[1,2,5])*cos(y[1,2,3,5])+sin(a[1,2,3])*sin(a[1,2,5]))+cos(a[1,2,3])*sin(y[1,2,3,5])*(L[1,2,5]+-1*cos(y[5,2,1,6])*L[6,2,5]))+cos(t[1,2,3,4])*cot(a[2,3,4])*1/r[2,3]+-1*L[1,2,3]*(cos(a[1,2,5])*sin(y[1,2,3,5])*sin(y[5,2,1,6])*L[6,2,5]+cos(y[1,2,3,5])*(L[1,2,5]+-1*cos(y[5,2,1,6])*L[6,2,5]))),
  (('t','y'),(1,2,3,4),(2,1,5,6)):csc(a[1,2,3])*1/m[1]*1/r[1,2]*(cos(t[3,2,1,5])*L[5,1,2]+-1*cos(t[3,2,1,5]+y[2,1,5,6])*L[6,1,2])+1/m[2]*1/r[1,2]*(cos(a[1,2,3])*cot(a[2,3,4])*1/r[2,3]*sin(t[1,2,3,4])*(cot(a[2,1,5])*sin(t[3,2,1,5])+-1*cot(a[2,1,6])*sin(t[3,2,1,5]+y[2,1,5,6]))+cos(t[3,2,1,5])*cot(a[2,1,5])+-1*cos(t[3,2,1,5]+y[2,1,5,6])*cot(a[2,1,6])*(cos(t[1,2,3,4])*cot(a[2,3,4])*1/r[2,3]+-1*L[1,2,3])),
  (('t','y'),(1,2,3,4),(5,1,2,6)):-1*csc(a[1,2,3])*1/m[1]*1/r[1,2]*(cos(t[3,2,1,5])*L[2,1,5]+-1*L[6,1,5]*(cos(t[3,2,1,5])*cos(y[5,1,2,6])+-1*cos(a[2,1,5])*sin(t[3,2,1,5])*sin(y[5,1,2,6])))+csc(a[2,1,5])*1/m[2]*1/r[1,2]*(cos(a[1,2,3])*cot(a[2,3,4])*1/r[2,3]*sin(t[1,2,3,4])*sin(t[3,2,1,5])+cos(t[3,2,1,5])*(cos(t[1,2,3,4])*cot(a[2,3,4])*1/r[2,3]+-1*L[1,2,3])),
  (('t','y'),(1,2,3,4),(3,2,5,6)):cos(t[1,2,3,4]+y[3,2,1,5])*(cot(a[3,2,5])*1/m[3]*1/r[3,2]*L[4,3,2]+cot(a[2,3,4])*1/m[2]*1/r[3,2]*L[5,2,3])+cos(y[3,2,1,5])*(-1*cot(a[3,2,1])*cot(a[3,2,5])*1/m[3]*1/r[3,2]**2+1/m[2]*L[1,2,3]*L[5,2,3])+-1*cos(t[1,2,3,4]+y[3,2,1,5]+y[3,2,5,6])*(cot(a[3,2,6])*1/m[3]*1/r[3,2]*L[4,3,2]+cot(a[2,3,4])*1/m[2]*1/r[3,2]*L[6,2,3])+cos(y[3,2,1,5]+y[3,2,5,6])*(cot(a[3,2,1])*cot(a[3,2,6])*1/m[3]*1/r[3,2]**2+1/m[2]*L[1,2,3]*L[6,2,3]),
  (('t','y'),(1,2,3,4),(5,2,3,6)):1/m[2]*(-1*cos(a[3,2,5])*sin(y[5,2,3,6])*L[6,2,5]*(cot(a[2,3,4])*1/r[3,2]*sin(t[5,2,3,4])+sin(t[1,2,3,4]+-1*t[5,2,3,4])*L[1,2,3])+-1*cos(t[5,2,3,4])*cot(a[2,3,4])*1/r[3,2]+cos(t[1,2,3,4]+-1*t[5,2,3,4])*L[1,2,3]*(L[3,2,5]+-1*cos(y[5,2,3,6])*L[6,2,5]))+csc(a[3,2,5])*1/m[3]*1/r[3,2]*(-1*cos(t[1,2,3,4]+-1*t[5,2,3,4])*cot(a[3,2,1])*1/r[3,2]+cos(t[5,2,3,4])*L[4,3,2]),
  (('t','y'),(1,2,3,4),(1,5,6,7)):csc(a[1,2,3])*1/m[1]*1/r[1,2]*1/r[1,5]*(cos(t[3,2,1,5])*(cos(t[2,1,5,6])*cot(a[1,5,6])+-1*cos(t[2,1,5,6]+y[1,5,6,7])*cot(a[1,5,7]))+cos(a[2,1,5])*sin(t[3,2,1,5])*(cot(a[1,5,6])*sin(t[2,1,5,6])+-1*cot(a[1,5,7])*sin(t[2,1,5,6]+y[1,5,6,7]))),
  (('t','y'),(1,2,3,4),(5,6,1,7)):csc(a[1,2,3])*csc(a[1,6,5])*1/m[1]*1/r[1,2]*1/r[1,6]*(cos(t[2,1,6,5])*cos(t[3,2,1,6])+cos(a[2,1,6])*sin(t[2,1,6,5])*sin(t[3,2,1,6])),
  (('t','y'),(1,2,3,4),(5,1,6,7)):-1*csc(a[1,2,3])*1/m[1]*1/r[1,2]*(L[6,1,5]*(cos(t[3,2,1,5])*cos(y[5,1,2,6])+-1*cos(a[2,1,5])*sin(t[3,2,1,5])*sin(y[5,1,2,6]))+-1*L[7,1,5]*(cos(t[3,2,1,5])*cos(y[5,1,2,6]+y[5,1,6,7])+-1*cos(a[2,1,5])*sin(t[3,2,1,5])*sin(y[5,1,2,6]+y[5,1,6,7]))),
  (('t','y'),(1,2,3,4),(3,5,6,7)):-1*1/m[3]*1/r[3,5]*(cos(t[2,3,5,6])*cot(a[3,5,6])+-1*cos(t[2,3,5,6]+y[3,5,6,7])*cot(a[3,5,7])*(-1*cos(t[1,2,3,5])*cot(a[3,2,1])*1/r[3,2]+cos(t[1,2,3,4]+-1*t[1,2,3,5])*L[4,3,2])+cos(a[2,3,5])*(cot(a[3,5,6])*sin(t[2,3,5,6])+-1*cot(a[3,5,7])*sin(t[2,3,5,6]+y[3,5,6,7]))*(-1*cot(a[3,2,1])*1/r[3,2]*sin(t[1,2,3,5])+-1*sin(t[1,2,3,4]+-1*t[1,2,3,5])*L[4,3,2])),
  (('t','y'),(1,2,3,4),(5,6,3,7)):-1*csc(a[3,6,5])*1/m[3]*1/r[3,6]*(cos(t[2,3,6,5])*(-1*cos(t[1,2,3,6])*cot(a[3,2,1])*1/r[3,2]+cos(t[1,2,3,4]+-1*t[1,2,3,6])*L[4,3,2])+cos(a[2,3,6])*sin(t[2,3,6,5])*(-1*cot(a[3,2,1])*1/r[3,2]*sin(t[1,2,3,6])+-1*sin(t[1,2,3,4]+-1*t[1,2,3,6])*L[4,3,2])),
  (('t','y'),(1,2,3,4),(5,3,6,7)):1/m[3]*(-1*cos(t[1,2,3,5])*cot(a[3,2,1])*1/r[3,2]+cos(t[1,2,3,4]+-1*t[1,2,3,5])*L[4,3,2]*(cos(y[5,3,2,6])*L[6,3,5]+-1*cos(y[5,3,2,6]+y[5,3,6,7])*L[7,3,5])+-1*cos(a[2,3,5])*(-1*cot(a[3,2,1])*1/r[3,2]*sin(t[1,2,3,5])+-1*sin(t[1,2,3,4]+-1*t[1,2,3,5])*L[4,3,2])*(sin(y[5,3,2,6])*L[6,3,5]+-1*sin(y[5,3,2,6]+y[5,3,6,7])*L[7,3,5])),
  (('y','y'),(1,2,3,4),(1,2,3,4)):csc(a[1,2,3])**2*1/m[3]*1/r[2,3]**2+csc(a[1,2,4])**2*1/m[4]*1/r[2,4]**2+1/m[2]*(L[3,2,1]**2+-2*cos(y[1,2,3,4])*L[3,2,1]*L[4,2,1]+L[4,2,1]**2)+1/m[1]*1/r[1,2]**2*(cot(a[1,2,3])**2+-2*cos(y[1,2,3,4])*cot(a[1,2,3])*cot(a[1,2,4])+cot(a[1,2,4])**2),
  (('y','y'),(1,2,3,4),(1,2,3,5)):csc(a[1,2,3])**2*1/m[3]*1/r[2,3]**2+1/m[2]*(cos(y[1,2,3,4]+-1*y[1,2,3,5])*L[4,2,1]*L[5,2,1]+L[3,2,1]*(L[3,2,1]+-1*cos(y[1,2,3,4])*L[4,2,1]+-1*cos(y[1,2,3,5])*L[5,2,1]))+1/m[1]*1/r[1,2]**2*(cos(y[1,2,3,4]+-1*y[1,2,3,5])*cot(a[1,2,4])*cot(a[1,2,5])+cot(a[1,2,3])*(cot(a[1,2,3])+-1*cos(y[1,2,3,4])*cot(a[1,2,4])+-1*cos(y[1,2,3,5])*cot(a[1,2,5]))),
  (('y','y'),(1,2,3,4),(3,2,1,5)):-1*1/m[2]*(cos(a[1,2,3])*sin(y[1,2,3,4])*sin(y[3,2,1,5])*L[4,2,1]*L[5,2,3]+L[3,2,1]+-1*cos(y[1,2,3,4])*L[4,2,1]*(L[1,2,3]+-1*cos(y[3,2,1,5])*L[5,2,3]))+csc(a[1,2,3])*1/m[1]*1/r[1,2]**2*(cot(a[1,2,3])+-1*cos(y[1,2,3,4])*cot(a[1,2,4]))+csc(a[1,2,3])*1/m[3]*1/r[2,3]**2*(cot(a[1,2,3])+-1*cos(y[3,2,1,5])*cot(a[3,2,5])),
  (('y','y'),(1,2,3,4),(1,2,5,6)):1/m[2]*(-1*L[4,2,1]*(cos(y[1,2,3,4]+-1*y[1,2,3,5])*L[5,2,1]+-1*cos(y[1,2,3,4]+-1*y[1,2,3,5]+-1*y[1,2,5,6])*L[6,2,1])+L[3,2,1]*(cos(y[1,2,3,5])*L[5,2,1]+-1*cos(y[1,2,3,5]+y[1,2,5,6])*L[6,2,1]))+1/m[1]*1/r[1,2]**2*(-1*cot(a[1,2,4])*(cos(y[1,2,3,4]+-1*y[1,2,3,5])*cot(a[1,2,5])+-1*cos(y[1,2,3,4]+-1*y[1,2,3,5]+-1*y[1,2,5,6])*cot(a[1,2,6]))+cot(a[1,2,3])*(cos(y[1,2,3,5])*cot(a[1,2,5])+-1*cos(y[1,2,3,5]+y[1,2,5,6])*cot(a[1,2,6]))),
  (('y','y'),(1,2,3,4),(5,2,1,6)):-1*1/m[2]*(cos(a[1,2,5])*sin(y[5,2,1,6])*L[6,2,5]*(sin(y[1,2,3,5])*L[3,2,1]+sin(y[1,2,3,4]+-1*y[1,2,3,5])*L[4,2,1])+cos(y[1,2,3,5])*L[3,2,1]+-1*cos(y[1,2,3,4]+-1*y[1,2,3,5])*L[4,2,1]*(L[1,2,5]+-1*cos(y[5,2,1,6])*L[6,2,5]))+csc(a[1,2,5])*1/m[1]*1/r[1,2]**2*(cos(y[1,2,3,5])*cot(a[1,2,3])+-1*cos(y[1,2,3,4]+-1*y[1,2,3,5])*cot(a[1,2,4])),
  (('y','y'),(1,2,3,4),(5,2,3,6)):cos(y[3,2,1,5])*csc(a[3,2,1])*csc(a[3,2,5])*1/m[3]*1/r[3,2]**2+1/m[2]*(sin(y[1,2,3,4])*sin(y[5,2,3,6])*L[4,2,1]*L[6,2,5]*(cos(a[3,2,1])*cos(a[3,2,5])*cos(y[3,2,1,5])+sin(a[3,2,1])*sin(a[3,2,5]))+cos(y[3,2,1,5])*(L[3,2,1]+-1*cos(y[1,2,3,4])*L[4,2,1])*(L[3,2,5]+-1*cos(y[5,2,3,6])*L[6,2,5])+sin(y[3,2,1,5])*(cos(a[3,2,5])*sin(y[5,2,3,6])*L[6,2,5]*(L[3,2,1]+-1*cos(y[1,2,3,4])*L[4,2,1])+-1*cos(a[3,2,1])*L[4,2,1]*sin(y[1,2,3,4])*(L[3,2,5]+-1*cos(y[5,2,3,6])*L[6,2,5]))),
  (('y','y'),(1,2,3,4),(2,1,5,6)):-1*1/m[1]*1/r[1,2]*(cot(a[1,2,3])*(cos(t[3,2,1,5])*L[5,1,2]+-1*cos(t[3,2,1,5]+y[2,1,5,6])*L[6,1,2])+-1*cot(a[1,2,4])*(cos(t[3,2,1,5]+y[1,2,3,4])*L[5,1,2]+-1*cos(t[3,2,1,5]+y[1,2,3,4]+y[2,1,5,6])*L[6,1,2]))+-1*1/m[2]*1/r[1,2]*(cot(a[2,1,5])*(cos(t[3,2,1,5])*L[3,2,1]+-1*cos(t[3,2,1,5]+y[1,2,3,4])*L[4,2,1])+-1*cot(a[2,1,6])*(cos(t[3,2,1,5]+y[2,1,5,6])*L[3,2,1]+-1*cos(t[3,2,1,5]+y[1,2,3,4]+y[2,1,5,6])*L[4,2,1])),
  (('y','y'),(1,2,3,4),(5,1,2,6)):1/m[1]*1/r[1,2]*(cos(a[2,1,5])*sin(y[5,1,2,6])*L[6,1,5]*(cot(a[1,2,3])*sin(t[3,2,1,5])+-1*cot(a[1,2,4])*sin(t[3,2,1,5]+y[1,2,3,4]))+cos(t[3,2,1,5])*cot(a[1,2,3])+-1*cos(t[3,2,1,5]+y[1,2,3,4])*cot(a[1,2,4])*(L[2,1,5]+-1*cos(y[5,1,2,6])*L[6,1,5]))+-1*csc(a[2,1,5])*1/m[2]*1/r[1,2]*(cos(t[3,2,1,5])*L[3,2,1]+-1*cos(t[3,2,1,5]+y[1,2,3,4])*L[4,2,1]),
  (('y','y'),(1,2,3,4),(5,3,2,6)):csc(a[2,3,5])*1/m[2]*1/r[3,2]*(cos(a[3,2,1])*sin(t[1,2,3,5])*sin(y[1,2,3,4])*L[4,2,1]+cos(t[1,2,3,5])*(L[3,2,1]+-1*cos(y[1,2,3,4])*L[4,2,1]))+csc(a[3,2,1])*1/m[3]*1/r[3,2]*(cos(a[2,3,5])*sin(t[1,2,3,5])*sin(y[5,3,2,6])*L[6,3,5]+cos(t[1,2,3,5])*(L[2,3,5]+-1*cos(y[5,3,2,6])*L[6,3,5])),
  (('y','y'),(1,2,3,4),(1,5,6,7)):-1*1/m[1]*1/r[1,2]*1/r[1,5]*(cos(t[3,2,1,5])*cot(a[1,2,3])+-1*cos(t[3,2,1,5]+y[1,2,3,4])*cot(a[1,2,4])*(cos(t[2,1,5,6])*cot(a[1,5,6])+-1*cos(t[2,1,5,6]+y[1,5,6,7])*cot(a[1,5,7]))+cos(a[2,1,5])*(cot(a[1,2,3])*sin(t[3,2,1,5])+-1*cot(a[1,2,4])*sin(t[3,2,1,5]+y[1,2,3,4]))*(cot(a[1,5,6])*sin(t[2,1,5,6])+-1*cot(a[1,5,7])*sin(t[2,1,5,6]+y[1,5,6,7]))),
  (('y','y'),(1,2,3,4),(5,6,1,7)):-1*csc(a[1,6,5])*1/m[1]*1/r[1,2]*1/r[1,6]*(cos(t[2,1,6,5])*(cos(t[3,2,1,6])*cot(a[1,2,3])+-1*cos(t[3,2,1,6]+y[1,2,3,4])*cot(a[1,2,4]))+cos(a[2,1,6])*sin(t[2,1,6,5])*(cot(a[1,2,3])*sin(t[3,2,1,6])+-1*cot(a[1,2,4])*sin(t[3,2,1,6]+y[1,2,3,4]))),
  (('y','y'),(1,2,3,4),(5,6,3,7)):-1*csc(a[3,2,1])*csc(a[3,6,5])*1/m[3]*1/r[3,2]*1/r[3,6]*(cos(t[1,2,3,6])*cos(t[2,3,6,5])+cos(a[2,3,6])*sin(t[1,2,3,6])*sin(t[2,3,6,5])),
  (('y','y'),(1,2,3,4),(5,1,6,7)):1/m[1]*1/r[1,2]*(cos(t[3,2,1,5])*cot(a[1,2,3])+-1*cos(t[3,2,1,5]+y[1,2,3,4])*cot(a[1,2,4])*(cos(y[5,1,2,6])*L[6,1,5]+-1*cos(y[5,1,2,6]+y[5,1,6,7])*L[7,1,5])+-1*cos(a[2,1,5])*(cot(a[1,2,3])*sin(t[3,2,1,5])+-1*cot(a[1,2,4])*sin(t[3,2,1,5]+y[1,2,3,4]))*(sin(y[5,1,2,6])*L[6,1,5]+-1*sin(y[5,1,2,6]+y[5,1,6,7])*L[7,1,5])),
  (('y','y'),(1,2,3,4),(5,3,6,7)):csc(a[3,2,1])*1/m[3]*1/r[3,2]*(cos(t[1,2,3,5])*(cos(y[5,3,2,6])*L[6,3,5]+-1*cos(y[5,3,2,6]+y[5,3,6,7])*L[7,3,5])+-1*cos(a[2,3,5])*sin(t[1,2,3,5])*(sin(y[5,3,2,6])*L[6,3,5]+-1*sin(y[5,3,2,6]+y[5,3,6,7])*L[7,3,5])),
  (('y','y'),(1,2,3,4),(5,2,6,7)):-1*1/m[2]*(cos(y[1,2,5,3])*L[3,2,1]+-1*cos(y[1,2,3,4]+y[1,2,5,3])*L[4,2,1]*(cos(y[5,2,1,6])*L[6,2,5]+-1*cos(y[5,2,1,6]+y[5,2,6,7])*L[7,2,5])+cos(a[1,2,5])*(sin(y[1,2,5,3])*L[3,2,1]+-1*sin(y[1,2,3,4]+y[1,2,5,3])*L[4,2,1])*(sin(y[5,2,1,6])*L[6,2,5]+-1*sin(y[5,2,1,6]+y[5,2,6,7])*L[7,2,5]))
}
vp = {
  (('r','r'),(1,2),(1,2)):0,
  (('r','r'),(1,2),(1,3)):cos(a[2,1,3])*1/m[1]*1/r[1,2]*1/r[1,3],
  (('r','a'),(1,2),(1,2,3)):-1*cos(a[1,2,3])*1/m[2]*1/r[1,2]*1/r[2,3],
  (('r','a'),(1,2),(1,3,4)):0.5*cos(t[2,1,3,4])*cot(a[1,3,4])*1/m[1]*1/r[1,2]*1/r[1,3]*sin(a[2,1,3]),
  (('r','a'),(1,2),(3,1,4)):0.5*cot(a[3,1,4])*g[(('r','a'),(1,2),(3,1,4))]*1/r[1,2]+-1*0.5*1/m[1]*1/r[1,2]*1/r[1,4]*sin(a[3,1,4])*(2*cos(a[2,1,3])*cos(a[3,1,4])+cos(y[3,1,2,4])*sin(a[2,1,3])),
  (('r','t'),(1,2),(1,2,3,4)):-0.5*cos(t[1,2,3,4])*cot(a[2,3,4])*1/m[2]*1/r[1,2]*1/r[2,3]*sin(a[1,2,3]),
  (('r','t'),(1,2),(3,2,1,4)):0,
  (('r','t'),(1,2),(1,3,4,5)):0,
  (('r','t'),(1,2),(3,4,1,5)):-0.5*cos(t[3,4,1,2]+-1*t[3,4,1,5])*1/m[1]*1/r[1,2]*sin(a[2,1,4])*L[5,1,4],
  (('r','y'),(1,2),(1,2,3,4)):0,
  (('r','y'),(1,2),(3,2,1,4)):-0.5*cos(y[3,2,1,4])*1/m[2]*1/r[1,2]*sin(a[1,2,3])*L[4,2,3],
  (('r','y'),(1,2),(1,3,4,5)):-0.5*cos(t[2,1,3,4]+y[1,3,4,5])*cot(a[1,3,5])*1/m[1]*1/r[1,2]*1/r[1,3]*sin(a[2,1,3]),
  (('r','y'),(1,2),(3,4,1,5)):0,
  (('r','y'),(1,2),(3,1,4,5)):-0.5*cos(y[3,1,2,4]+y[3,1,4,5])*1/m[1]*1/r[1,2]*sin(a[2,1,3])*L[5,1,3],
  (('a','a'),(1,2,3),(1,2,3)):0.5*cos(a[1,2,3])*1/m[2]*1/r[1,2]*1/r[2,3]+-0.125*g[(('a','a'),(1,2,3),(1,2,3))]*(2+cot(a[1,2,3])**2),
  (('a','a'),(1,2,3),(2,1,4)):0.25*cot(a[1,2,3])*cot(a[2,1,4])*g[(('a','a'),(1,2,3),(2,1,4))]+-0.25*cos(t[3,2,1,4])*1/r[1,2]*(cot(a[2,1,4])*1/m[2]*1/r[2,3]*sin(a[1,2,3])+cot(a[1,2,3])*1/m[1]*1/r[1,4]*sin(a[2,1,4])),
  (('a','a'),(1,2,3),(1,2,4)):0.25*cot(a[1,2,3])*cot(a[1,2,4])*g[(('a','a'),(1,2,3),(1,2,4))]+0.25*1/m[2]*1/r[2,3]*1/r[2,4]*(2*cos(a[1,2,3])*cos(a[1,2,4])+cos(y[1,2,3,4])*(cos(a[1,2,3])*r[2,3]*sin(a[1,2,4])*L[1,2,3]+cos(a[1,2,4])*r[2,4]*sin(a[1,2,3])*L[1,2,4])),
  (('a','a'),(1,2,3),(1,4,5)):0.25*cot(a[1,2,3])*cot(a[1,4,5])*g[(('a','a'),(1,2,3),(1,4,5))],
  (('a','a'),(1,2,3),(4,1,5)):0.25*cot(a[1,2,3])*cot(a[4,1,5])*g[(('a','a'),(1,2,3),(4,1,5))]+-1*0.25*cot(a[1,2,3])*1/m[1]*1/r[1,2]*1/r[1,5]*(cos(t[3,2,1,4])*cos(a[4,1,5])*sin(a[2,1,4])+sin(a[4,1,5])*(-1*cos(t[3,2,1,4])*cos(a[2,1,4])*cos(y[4,1,2,5])+sin(t[3,2,1,4])*sin(y[4,1,2,5]))),
  (('a','a'),(1,2,3),(4,2,5)):0.25*cot(a[1,2,3])*cot(a[4,2,5])*g[(('a','a'),(1,2,3),(4,2,5))]+0.25*1/m[2]*(cos(a[1,2,3])*cos(a[4,2,5])*sin(a[1,2,4])*(cos(y[1,2,3,4])*1/r[2,5]*L[1,2,3]+cos(y[4,2,1,5])*1/r[2,3]*L[4,2,5])+-1*cos(a[1,2,4])*cos(y[1,2,3,4])*cos(y[4,2,1,5])+sin(y[1,2,3,4])*sin(y[4,2,1,5])*(cos(a[1,2,3])*1/r[2,5]*sin(a[4,2,5])*L[1,2,3]+cos(a[4,2,5])*1/r[2,3]*sin(a[1,2,3])*L[4,2,5])+1/r[2,3]*1/r[2,5]*(2*cos(a[1,2,3])*cos(a[1,2,4])*cos(a[4,2,5])+sin(a[1,2,4])*(cos(a[4,2,5])*cos(y[1,2,3,4])*sin(a[1,2,3])+cos(a[1,2,3])*cos(y[4,2,1,5])*sin(a[4,2,5])))),
  (('a','t'),(1,2,3),(1,2,3,4)):0.25*cos(t[1,2,3,4])*cot(a[1,2,3])*1/r[2,3]*(cot(a[2,3,4])*1/m[2]*sin(a[1,2,3])*L[3,2,1]+-1*1/m[3]*L[4,3,2]),
  (('a','t'),(1,2,3),(2,1,4,5)):0.25*cot(a[1,2,3])*cot(a[1,4,5])*1/m[1]*1/r[1,2]*1/r[1,4]*(cos(t[2,1,4,5])*cos(t[3,2,1,4])*cos(a[2,1,4])+sin(t[2,1,4,5])*sin(t[3,2,1,4])),
  (('a','t'),(1,2,3),(4,2,1,5)):-0.25*cos(t[3,2,1,5]+-1*t[4,2,1,5])*cot(a[1,2,3])*(cot(a[1,2,4])*1/m[1]*1/r[1,2]**2+-1*1/m[2]*sin(a[1,2,3])*L[1,2,3]*L[4,2,1]),
  (('a','t'),(1,2,3),(1,2,4,5)):0.25*cos(a[1,2,3])*cot(a[2,4,5])*1/m[2]*1/r[2,4]*(cos(t[1,2,4,5])*1/r[2,3]*sin(a[1,2,4])+-1*L[1,2,3]*(cos(t[1,2,4,5])*cos(a[1,2,4])*cos(y[1,2,3,4])+sin(t[1,2,4,5])*sin(y[1,2,3,4]))),
  (('a','t'),(1,2,3),(1,4,5,6)):0,
  (('a','t'),(1,2,3),(4,5,1,6)):0.25*cot(a[1,2,3])*1/m[1]*1/r[1,2]*L[6,1,5]*(cos(t[3,2,1,5])*cos(t[2,1,5,4]+-1*t[4,5,1,6])*cos(a[2,1,5])+sin(t[3,2,1,5])*sin(t[2,1,5,4]+-1*t[4,5,1,6])),
  (('a','t'),(1,2,3),(2,4,5,6)):0,
  (('a','t'),(1,2,3),(4,5,2,6)):0.25*1/m[2]*L[6,2,5]*cos(a[1,2,3])*(sin(t[1,2,5,4]+-1*t[4,5,2,6])*sin(y[1,2,5,3])*L[1,2,3]+cos(t[1,2,5,4]+-1*t[4,5,2,6])*(1/r[2,3]*sin(a[1,2,5])+-1*cos(a[1,2,5])*cos(y[1,2,5,3])*L[1,2,3])),
  (('a','y'),(1,2,3),(1,2,3,4)):0.25*cos(y[1,2,3,4])*cot(a[1,2,3])*(-1*cot(a[1,2,4])*1/m[1]*1/r[1,2]**2+1/m[2]*sin(a[1,2,3])*L[1,2,3]*L[4,2,1]),
  (('a','y'),(1,2,3),(2,1,4,5)):-0.25*cos(t[3,2,1,4]+y[2,1,4,5])*cot(a[1,2,3])*1/r[1,2]*(-1*cot(a[2,1,5])*1/m[2]*sin(a[1,2,3])*L[1,2,3]+1/m[1]*L[5,1,2]),
  (('a','y'),(1,2,3),(4,1,2,5)):-1*0.25*cot(a[1,2,3])*1/m[1]*1/r[1,2]*L[5,1,4]*(-1*cos(t[3,2,1,4])*cos(a[2,1,4])*cos(y[4,1,2,5])+sin(t[3,2,1,4])*sin(y[4,1,2,5])),
  (('a','y'),(1,2,3),(1,2,4,5)):-0.25*cos(y[1,2,3,4]+y[1,2,4,5])*(cot(a[1,2,3])*cot(a[1,2,5])*1/m[1]*1/r[1,2]**2+-1*cos(a[1,2,3])*1/m[2]*L[1,2,3]*L[5,2,1]),
  (('a','y'),(1,2,3),(4,2,1,5)):0.25*cos(a[1,2,3])*1/m[2]*L[5,2,4]*(cos(y[4,2,1,5])*1/r[2,3]*sin(a[1,2,4])+L[1,2,3]*(-1*cos(a[1,2,4])*cos(y[1,2,3,4])*cos(y[4,2,1,5])+sin(y[1,2,3,4])*sin(y[4,2,1,5]))),
  (('a','y'),(1,2,3),(1,4,5,6)):0.25*cot(a[1,2,3])*cot(a[1,4,6])*1/m[1]*1/r[1,2]*1/r[1,4]*(cos(t[3,2,1,4])*cos(a[2,1,4])*cos(t[2,1,4,5]+y[1,4,5,6])+sin(t[3,2,1,4])*sin(t[2,1,4,5]+y[1,4,5,6])),
  (('a','y'),(1,2,3),(4,5,1,6)):0,
  (('a','y'),(1,2,3),(4,1,5,6)):-1*0.25*cot(a[1,2,3])*1/m[1]*1/r[1,2]*L[6,1,4]*(-1*cos(t[3,2,1,4])*cos(a[2,1,4])*cos(y[4,1,2,5]+y[4,1,5,6])+sin(t[3,2,1,4])*sin(y[4,1,2,5]+y[4,1,5,6])),
  (('a','y'),(1,2,3),(2,4,5,6)):0.25*cos(a[1,2,3])*1/m[2]*1/r[2,4]*cot(a[2,4,6])*(sin(y[1,2,4,3])*sin(t[1,2,4,5]+y[2,4,5,6])*L[1,2,3]+cos(t[1,2,4,5]+y[2,4,5,6])*(1/r[2,3]*sin(a[1,2,4])+-1*cos(a[1,2,4])*cos(y[1,2,4,3])*L[1,2,3])),
  (('a','y'),(1,2,3),(4,5,2,6)):0,
  (('a','y'),(1,2,3),(4,2,5,6)):-0.25*1/m[2]*L[6,2,4]*cos(a[1,2,3])*(sin(y[1,2,4,3])*sin(y[4,2,1,5]+y[4,2,5,6])*L[1,2,3]+cos(y[4,2,1,5]+y[4,2,5,6])*(-1*1/r[2,3]*sin(a[1,2,4])+cos(a[1,2,4])*cos(y[1,2,4,3])*L[1,2,3])),
  (('t','t'),(1,2,3,4),(1,2,3,4)):0,
  (('t','t'),(1,2,3,4),(1,2,3,5)):0,
  (('t','t'),(1,2,3,4),(3,2,1,5)):0,
  (('t','t'),(1,2,3,4),(1,2,5,6)):0,
  (('t','t'),(1,2,3,4),(5,2,1,6)):0,
  (('t','t'),(1,2,3,4),(2,1,5,6)):0,
  (('t','t'),(1,2,3,4),(5,2,3,6)):0,
  (('t','t'),(1,2,3,4),(1,5,6,7)):0,
  (('t','t'),(1,2,3,4),(5,6,1,7)):0,
  (('t','t'),(1,2,3,4),(5,6,3,7)):0,
  (('t','y'),(1,2,3,4),(1,2,3,5)):0,
  (('t','y'),(1,2,3,4),(3,2,1,5)):0,
  (('t','y'),(1,2,3,4),(1,2,5,6)):0,
  (('t','y'),(1,2,3,4),(5,2,1,6)):0,
  (('t','y'),(1,2,3,4),(2,1,5,6)):0,
  (('t','y'),(1,2,3,4),(5,1,2,6)):0,
  (('t','y'),(1,2,3,4),(3,2,5,6)):0,
  (('t','y'),(1,2,3,4),(5,2,3,6)):0,
  (('t','y'),(1,2,3,4),(1,5,6,7)):0,
  (('t','y'),(1,2,3,4),(5,6,1,7)):0,
  (('t','y'),(1,2,3,4),(5,1,6,7)):0,
  (('t','y'),(1,2,3,4),(3,5,6,7)):0,
  (('t','y'),(1,2,3,4),(5,6,3,7)):0,
  (('t','y'),(1,2,3,4),(5,3,6,7)):0,
  (('y','y'),(1,2,3,4),(1,2,3,4)):0,
  (('y','y'),(1,2,3,4),(1,2,3,5)):0,
  (('y','y'),(1,2,3,4),(3,2,1,5)):0,
  (('y','y'),(1,2,3,4),(1,2,5,6)):0,
  (('y','y'),(1,2,3,4),(5,2,1,6)):0,
  (('y','y'),(1,2,3,4),(5,2,3,6)):0,
  (('y','y'),(1,2,3,4),(2,1,5,6)):0,
  (('y','y'),(1,2,3,4),(5,1,2,6)):0,
  (('y','y'),(1,2,3,4),(5,3,2,6)):0,
  (('y','y'),(1,2,3,4),(1,5,6,7)):0,
  (('y','y'),(1,2,3,4),(5,6,1,7)):0,
  (('y','y'),(1,2,3,4),(5,6,3,7)):0,
  (('y','y'),(1,2,3,4),(5,1,6,7)):0,
  (('y','y'),(1,2,3,4),(5,3,6,7)):0,
  (('y','y'),(1,2,3,4),(5,2,6,7)):0
}

data = {k:(g[k], vp[k]) for k in g}