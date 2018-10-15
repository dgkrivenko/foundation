# put your python code here
a = input().split()
b = [int(i) for i in a]

def check(b):
    sum = 0
    if len(b) == 0:
        return True
    for i in range(1, len(b)):
        sum += b[i]
    if sum == b[0] and len(b) == ((b[0] * 2) + 1):
        return True
    else :
        return False
if check(b):
    print(1)
    
else:
    print(0)