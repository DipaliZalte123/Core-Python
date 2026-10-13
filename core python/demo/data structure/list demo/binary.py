
def binarySearch(li, search_else):
    beg = 0
    end = len(li) -1
    while(beg <= end):
    mid = (beg + end) //2
    if(search_else == li[mid]):
        return mid
    elif(search_else < li[mid]):
        end = mid - 1
    elif(search_else > li[mid]):
        beg = mid + 1
    else:
        return -1

    li = [10, 20, 30, 40, 50, 60]
    ele = int(input('Enter element to find:'))
res = binarySearch(li,else)
if(res != -1):
    print(f'{else} is present at index {res}.')
else:
    print(f'{else} is not present in the list.')
    