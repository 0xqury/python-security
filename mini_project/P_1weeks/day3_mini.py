select = -1 # 메뉴 선택값 변수 선언.
H_List = [] # 사람 명단 변수 선언.
try:        # 예외처리
    while select != 0:  # select가 0일 시 반복문 종료.
        print("==================================================")
        print("                       Menu")
        print("==================================================")
        print("1 : 출석 추가 | 2 : 명단 출력 | 0 : 프로그램 종료")
        print("==================================================")
        select = int(input("메뉴를 선택하세요 : "))
        if select == 1:     # H_List에 이름 추가.
            H_List.append(str(input("명단에 추가할 이름을 입력하세요 : ")))
        elif select == 2:   # H_List 명단 출력.
            if len(H_List) == 0 :   # 명단이 존재하지 않을 시 countunue 실행.
                print("명단이 존재하지 않습니다.")
                continue
            print(f"출석자 명단 : [", end = "")
            for i in range(0, len(H_List)): # for문을 이용하여 명단 출력.
                if i == len(H_List)-1 or len(H_List) == 1:  # 자연스런 출력을 위해 조건 설정.
                    print(f"\'{H_List[i]}\'", end="")
                else:
                    print(f"\'{H_List[i]}\', ", end="")
            print("]")
        elif select == 0:
            print("프로그램 종료.")
            break
except:
    print("잘못된 입력입니다.")