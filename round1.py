a = list(map(int,input("\nEnter the elements for array a: ").strip().split()))
print(a)
n1 = int(input('Enter a number: '))

def function1(n1,a) :
 length = len(a)
 if n1 in a:     
   for i in range (length):
        if a[i] == n1:
           print("Index of",n1,"is",i)
 if n1 not in a:
    for i in range (length):
        if a[i] > n1:
          index = i
          print("Index of",n1,"is",index)
          break

 if n1 > a[length-1]:
    index = length
    print("Index of",n1,"is",index)
function1(n1,a)
          
          
