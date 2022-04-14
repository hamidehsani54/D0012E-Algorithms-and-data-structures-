import sys

def print3smal(lst, arr_size):
    count = 0
    if (arr_size < 3):
        print(" Invalid Input ")
        return
    else:
        third = first = second = sys.maxsize


        for i in range(0, arr_size):
            count = count + 1
            if (lst[i] < first):
                third = second
                second = first
                first = lst[i]

            elif (lst[i] < second):

                third = second
                second = lst[i]

            elif (lst[i] < third):
                third = lst[i]

        return (first,second,third)


print(print3smal([10,6,2,4,6,78,8,5,3,2,5,7], 12))

def divideAndConquer (lst, svararr):

    if len(lst) <= 1:
        print("Listan är för kort!")
        return
    else:
        if len(lst) <= 3:

            for i in range(0, len(lst)):

                if (lst[i] < svararr[0]):
                    svararr[2] = svararr[1]
                    svararr[1] = svararr[0]
                    svararr[0] = lst[i]

                elif (lst[i] < svararr[1]):
                    svararr[2] = svararr[1]
                    svararr[1] = lst[i]

                elif (lst[i] < svararr[2]):
                    svararr[2] = lst[i]

            return svararr
        else:

            mid = len(lst) // 2
            R = lst[mid:]
            L = lst[:mid]

            divideAndConquer(L,svararr)
            divideAndConquer(R,svararr)

        return("tre minsta element är ", svararr[0],svararr[1],svararr[2])

print(divideAndConquer([10,6,2,4,6,78,8,5,3,2,5,7],[sys.maxsize,sys.maxsize,sys.maxsize]))

def algo1(lst):
    # O(n)
    if len(lst)==2: #Base case for even number of inputs
        return(lst[1] / lst[0])
    if len(lst)==3: #Base case for odd number of inputs
        return max(lst[1] / lst[0], lst[2] / lst[0], lst[2] / lst[1])

    mid = len(lst)//2
    lpos = algo1(lst[:mid])         #Each recursive step divides the given list into two steps, left and right side
    rpos = algo1(lst[mid:])

    leftMin = min(lst[:mid])
    rightM = max(lst[mid:])             #We want to find the highest value of the right side (nominator) divided by the left side (denominator) recursively.
    maxP = max(lpos, rpos, rightM / leftMin)
    return (maxP, int(leftMin), int(rightM))                         #continue until the base case is met ( 3 >= len(lst) >= 2 )
#print(algo1([10,6,2,4,6,78,8,5,3,2,5,7]))
