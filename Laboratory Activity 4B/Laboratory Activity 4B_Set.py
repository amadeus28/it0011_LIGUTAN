A = {"a", "b", "c", "d", "f", "g"}
B = {"b", "c", "h", "l", "m", "o"}
C = {"c", "d", "f", "h", "j", "k", "i"}

print("a. How many elements are there in set A and B?")
print("  ", len(A.union(B)))

print("\nb. How many elements are there in B that are not part of A and C?")
print("  ", len(B.difference(A, C)), "\n")

print("c. Show the following using set operations")
print("i.", C.difference(A))     
print("ii.", A.intersection(C))            
print("iii.", B.intersection(A.union(C)))  
print("iv.", A.intersection(C).difference(B))  
print("v.", A.intersection(B, C))          
print("vi.", B.difference(A.union(C)))  
