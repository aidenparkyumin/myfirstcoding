import random

cChoice=random.choice("SRP")

print("가위,바위,보?")
uChoice=input("S(가위), R(바위), P(보) 중 하나를 고르세요: ").upper().strip()

print("유민이: ", uChoice)
print("컴퓨터: ", cChoice)

if uChoice==cChoice:
    print("무승부 입니다")
else:
    if cChoice=="S":
        if uChoice=="R":
            print("win!")
        elif uChoice=="P":
            print("lose")
    elif cChoice=="R":
        if uChoice=="P":
            print("win!")
        elif uChoice=="S":
            print("lose")
    elif cChoice=="P":
        if uChoice=="S":
            print("win!")
        elif uChoice=="R":
            print("lose")