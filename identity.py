#identity operator
##--- is
##--- is not
##object id and datatype
##datatype 2\ type
##mutable and immutable

a=10
b=10
c=20
print(a is b)
print(a is c)
print(id(a))
print(id(b))
a=[1,3,4]
b=[1,3,4]
c=a
print(a is b)
print(id(a))
print(id(b))
print(a is c)
print(id(a))
print(id(b))

