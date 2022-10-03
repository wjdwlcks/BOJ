#def recursion(s, l, r, cnt):    
#    if l >= r: return 1, cnt
#    elif s[l] != s[r]: return 0, cnt
#    else: return recursion(s, l+1, r-1,cnt+1)
#
#def isPalindrome(s):
#    return recursion(s, 0, len(s)-1,1)
#
#
#for i in range(int(input())):
#    a,b =isPalindrome(input())
#    print(a,b)


# import sys
# input = sys.stdin.readline

# def recursion(s, l, r):
#     global cnt # 함수 내에서 전역 변수로 cnt를 활용하기 위해 global로 명시해준다.
#     cnt += 1
    
#     if l >= r: return 1
#     elif s[l] != s[r]: return 0
#     else: return recursion(s, l+1, r-1)

# def isPalindrome(s):
#     return recursion(s, 0, len(s)-1)

# for _ in range(int(input())):
#     cnt = 0
#     print(isPalindrome(input().rstrip()), cnt)



#def recursion(s: str, l: int, r: int, cnt: int):
#    cnt += 1
#    if l >= r:
#        return 1, cnt
#    elif s[l] != s[r]:
#        return 0, cnt
#    return recursion(s, l+1, r-1, cnt)
#
#def isPalindrome(s: str, cnt: int):
#    return recursion(s, 0, len(s)-1, cnt)
#
#if __name__ == '__main__':
#    t = int(input())  # 테스트케이스의 개수
#
#    for _ in range(t):
#        s = str(input())  # 문자열 s
#        cnt = 0           # recursion 호출 횟수
#        print(*isPalindrome(s, cnt))    
