def cal():
    try:
        oriMon = input("금액을 입력해주세요")
        print(oriMon + "원을 계산하려면")
        print("1000원권 지폐 " + oriMon[0] + "장")
        print("100원 동전 " + oriMon[1] + "개")
        print("10원 동전 " + oriMon[2] + "개가 필요합니다.")
    except:
        print("가 필요합니다.")
    
cal()