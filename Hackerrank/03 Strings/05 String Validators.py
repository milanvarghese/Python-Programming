if __name__ == '__main__':
    s = input()
    a,b,c,d,e=False,False,False,False,False
    if 0<len(s) and len(s)<1000:
        for i in s:
            if (i.isalnum()):
                a=True
            if (i.isalpha()):
                b=True
            if (i.isdigit()):
                c=True
            if (i.islower()):
                d=True
            if (i.isupper()):
                e=True
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)