#triangle
'''
for n = 5
*
**
***
****
*****

'''
def triangle(n):
    # first half
    print("Ascending")
    for i in range(n+1):
        print('*'*i)
    # reverse
    print("\nDescending\n")
    for i in range(n,0,-1):
        print('*'*i)
# pyramid
'''

for n = 5
    *
   ***
  *****
 *******
*********

'''
def pyramid(n):
    print()
    for i in range(1,n+1):
        print(' '*(n-i),'*'*i,'*'*(i-1),sep="")
# diamond pattern
'''
for n = 5
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
    
'''
def diamond(n):
    print()
    # first half
    for i in range(1, n+1):
        print(' ' * (n-i), '*' * i, '*' * (i-1), sep="")
    # second half
    for i in range(n-1, 0, -1):
        print(' ' * (n-i), '*' * i, '*' * (i-1), sep="")

# box pattern
'''
for n = 5
*****
*   *
*   *
*   *
*****
'''
def box(n):
    print()
    for i in range(1,n+1):
        if i == 1 or i == n:
            print('*' * n)
        else:
            for j in range(1,n+1):
                if j == 1:
                    print('*', end="")
                elif j == n:
                    print('*')
                else:
                    print(' ', end="")

# inverse diamond
'''
for n = 5
**** ****
***   ***
**     **
*       *
**     **
***   ***
**** ****
'''
def invdia(n):
    print()
    # first half
    for i in range(1,n*2):
        if i < n:
            print('*' * (n-i), ' ' * (i*2-1), '*' * (n-i), sep="")
        elif i > n and i != (2*n)-1:
            print('*' * ((i-n)+1), ' ' * (2*n-i-1), ' ' * ((2*n-1)-i-1), '*' * ((i-n)+1), sep="")



if __name__ == '__main__':
    funcs = {
        "Astericks Right Angled Triangle" : triangle,
        "Astericks Pyramid" : pyramid,
        "Diamond Pattern" : diamond,
        "Box pattern":box,
        "Inverted Diamond" : invdia
        }
    for i,j in zip(funcs,range(len(funcs))):
        print(j,i)
    ch = int(input("Enter your choice: "))
    for i,j in zip(funcs,range(len(funcs))):
        if j == ch:
            x=funcs[i]
    x(int(input("Enter number: ")))
