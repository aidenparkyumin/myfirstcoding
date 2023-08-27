i = 0
while True:
    print('knock')
    if i>=3:
        break
    i=i+1

for i in range(1, 5):
    if i==3:
        break
    print(i)
print('i가 3입니다')

i =1
while True:
    print(i, '월 1만원을 입금했습니다.')
    if i==12:
        print('입금완료! 12만원을 수량하세요!')
        break
    i=i+1


i=1
sum=0
while True:
    sum=sum+i
    if i >= 10:
        break
    i=i+1
print(sum)