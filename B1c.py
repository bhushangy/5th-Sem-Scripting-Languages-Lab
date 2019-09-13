n = int(input("enter size: "))
lis = []
for i in range(0,n):
    inp = int(input())
    lis.append(inp)
n = len(lis)

def find_max(lis, n): 
      
    # if size = 0 means whole array 
    # has been traversed 
    if (n == 1): 
        return lis[0] 
    return max(lis[n - 1], find_max(lis, n - 1)) 

# if lis = [1,4,99,-3,3,5]
# return max(4,1) so returns 4
# next frame max(99,4) so returns 99
# next frame max(-3,99) so returns 99
# next frame max(3,99) so returns 99
# next frame max(5,99) so returns 99

print("max: ",find_max(lis,n))