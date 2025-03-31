# ID와 PW를 미리 설정해두고, 사용자 입력과 비교하여 로그인 성공/실패를 판단하시오.
# 기회는 최대 3번까지 허용.
chance = 0
info = {"ID":"guest", "PW":"guest123"} # 딕셔너리를 사용하여 ID와 PW 설정. 

while chance != 3:  # 3번의 기회까지 아이디와 비밀번호를 입력받는 반복문. 
    input_id = input("아이디를 입력하세요 : ")
    input_pw = input("비밀번호를 입력하세요 : ")

    if info["ID"] == input_id and info["PW"] == input_pw :  # ID와 PW가 DB 정보와 맞는지 확인. 
        print("로그인에 성공하였습니다.")
        break   # 성공시 반복문 중지.  
    else:
        print("로그인에 실패하였습니다.")
    chance += 1 # 실패 시 chance를 1 더하고 반복. 
if chance == 3: # 반복문 탈출 후 chance가 3이라면 실패사유 출력.
    print("\n로그인을 3회 실패하셨습니다.")
    print("프로그램을 종료합니다.")