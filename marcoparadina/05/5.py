# The first line is a bit of an unneccessary flex but ok
arr = [int( line.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2) for line in open('marcoparadina/5/input5.txt')]
arr.sort()
print('Solution to part 1:', arr[-1])
for i in range(len(arr)):
    if (arr[i+1])!=(arr[i]+1):
        print('Solution to part 2:', arr[i]+1)  
        break                                       