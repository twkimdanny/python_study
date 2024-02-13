hamburger = 0
cola = 0
fry = 0

while True:
    print("******************")
    print("메뉴를 선택하세요  ")
    print("1. 햄버거 (7,000원)")
    # print("2. 콜라  (1,000원)")
    # print("3. 감튀  (2,000원)")
    print("9. 종료")
    print("******************")

    menu = input("메뉴를 선택해 주세요 : ")
    print(menu + " 번을 선택하셨습니다.")
    
    if menu == '1' :
        # hamburger += 1
        hamburger = hamburger + 1

    print("현재 담은 물건 햄버거 : ",hamburger,"개")
    print("현재 계산할 가격은 : ",hamburger * 7000,"입니다.")
    
    if menu == '9' :
        print("9번을 선택하셨으니 종료하겠습니다.")
        break
    

