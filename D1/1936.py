A, B = map(int, input().split())
if A > B and A - B == 1:
    print('A')
elif B > A and B - A == 1:
    print('B')
elif A > B and A - B == 2 :
    print('B')
else:
    print('A')
