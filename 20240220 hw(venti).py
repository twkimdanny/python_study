hamburger = 0
cola = 0
fry = 0



while True:
    print("********************")
    print("  메뉴를 선택하세요  ")
    print("1. 햄버거 (7,000원)")
    print("2. 콜라   (1,000원)")
    print("3. 감튀   (3,500원)")
    print("9. 선택완료        ")
    print("********************")

    menu = input("매뉴를 선택해주세요 : ")
    
    

    print(menu + "번을 선택했습니다.")
    
    if menu == '1' :
        # hamburger += 1
        hamburger = hamburger + 1
        
        
    elif menu == '2' :
        cola = cola + 1
        
        
    elif menu == '3' :
        fry = fry + 1
    
    elif menu > '3' and menu < '9' :
        print("**ERROR** 1~3번 중에 선택해주세요!")
    
    
    print("현재 담은 물건 햄버거" , hamburger, "개", "콜라" , cola, "개", "감자튀김", fry, "개")
        
        
    
    if menu == '9' :
        print("메뉴선택을 종료하고 결제로 넘어가겠습니다.")
        print(">>>총액", hamburger*7000 + cola*1000 + fry*3500, "원")    
        break



    # amount = int(input("금액을 입력하세요 : "))

