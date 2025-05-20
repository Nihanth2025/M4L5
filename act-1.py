n1=[1,8,2]
n2=[2,9,3]
s=map(lambda x,y:x+y,n1,n2)
print("Sum list:",list(s))

k={2,3,4,9}
def cube(n):
    return n*n*n
re=list(map(cube,k))
print("Result:",re)