import random

def binarySearch(numberlist, l, r, searchedvalue):

    if r >= l:

        mid = l + (r - l) // 2

        if numberlist[mid] == searchedvalue:
            return mid

        elif numberlist[mid] > searchedvalue:
            return binarySearch(numberlist, l, mid-1, searchedvalue)

        else:
            return binarySearch(numberlist, mid+1, r, searchedvalue)

    else:
        return -1

numberlist = random.sample(range(0,1000),1000)

searchedvalue = random.randint(0,1000)

result = binarySearch(numberlist, 0, len(numberlist)-1,searchedvalue)

if result != -1:
    print('Element found!')

else:
    print('Not found')
   
