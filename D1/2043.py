K, P = map(int, input().split())
cnt = 1
while P != K:
    cnt += 1
    P += 1
    
print(cnt)

#print(P-K+1)