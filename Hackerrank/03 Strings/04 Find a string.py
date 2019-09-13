def count_substring(string, sub_string):
    n=0
    s=len(string)
    ss=len(sub_string)
    if s<=200 and s>=1:
        for i in range(0,s):
            x=string[i:i+ss]
            if x==sub_string:
                n+=1
        return n

if __name__ == '__main__':