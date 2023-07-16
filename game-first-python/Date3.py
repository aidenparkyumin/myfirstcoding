import datetime

today=datetime.datetime.now()

if today.weekday() in [5,6]:
    print("주말이므로 학교에 갑니다!")
    print("온종일 숙제하고 게임하며 지낼 수 있어요!")
elif today.weekday()==4:
    print("금요일이므로 내일이면 코딩하며 샷건칠 수 있어요!")
else:
    print("오늘은 학교가는 날입니다")