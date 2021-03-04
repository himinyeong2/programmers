def move(n, start, to):
    print("선반 "+ str(n) + "을 ["+ start + "] 에서 ["+to+"] 로 이동")

def hanoi(n, start, to, via):
    if(n==1):
        move(1, start, to)
    else:
        hanoi(n-1, start, via , to)
        move(n, start, to)
        hanoi(n-1, via, to, start)
        
if __name__ == "__main__":
    hanoi(3, 'A', 'C', 'B')


