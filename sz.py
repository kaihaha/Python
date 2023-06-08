a=(1,2,3,4,5,6)
b='Python'
c=zip(a,b)
print(c)
b1={'x':1,'y':2,'z':3}
b_1=['x','y','z']
b_2=[1,2,3]
b2=dict(zip(b_1,b_2))
print(b2)
c1={'x':1,'y':2,'z':3,'v':4}
# c1['x']
# c1['y']
# c1['z']
# c1['v']
del(c1['x'])
print(c1)
a_a,b_b,c_c={'x':1,'y':2,'z':3,'v':4}
a_a=['a']+['b']
