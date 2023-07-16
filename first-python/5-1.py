# if i >=90:
#     print('A')
# elif i >=75:
#     print('B')

# x=int(input())
# if x % 2== 0:
#     print('2의 배수입니다')
# elif x % 3==0:
#     print('3의 배수입니다')
# elif x % 3.5==0:
#     print('3.5의 배수입니다')

import random

ans = random.randrange(1,51)

while True:

    num =int(input("숫자를 입력하세용"))

    if num > ans:  
        print('그수보다 작음 ㅋ')
    elif num < ans:  
        print ('그수보다 큼 ㅋㅋㄹㅃㅃ 에휴 운도 없네 운도 없어')
    else:
        print('와 드디어 맞췄네 운없는놈아')
        break
  

