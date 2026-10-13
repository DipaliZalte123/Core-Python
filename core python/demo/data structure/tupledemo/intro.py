#1. ()
tu = (10,)  #use comma for single variable
tu = (10, 20, 30, 'a', 3.14)
print(type(tu))
print(tu)

#1. Heterogenous

#2. Immutable

#3. Duplicate elements are allowed
import sys
li = []
tu = ()
print(type(tu))
print(tu)
print(sys.getsizeof(li))
print(sys.getsizeof(tu))
