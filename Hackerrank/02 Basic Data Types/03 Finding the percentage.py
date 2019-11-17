if __name__ == '__main__':
    n = int(input())
    sm = {}

    for _ in range(n):
        name, line = input().split()
        scores = list(map(float, line))
        sm[name] = scores
    query_name = input()
    for i in sm:
        if i==query_name:
            x=float(sm[i][0])
            y=float(sm[i][1])
            z=float(sm[i][2])
            if x>=0 and x<=100 and y>=0 and y<=100 and z>=0 and z<=100:
                avg=(x+y+z)/3.0
                print("%.2f"%avg)
