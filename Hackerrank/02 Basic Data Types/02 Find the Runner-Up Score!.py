if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    m=arr.index(max(arr))
    print(arr[m-1])