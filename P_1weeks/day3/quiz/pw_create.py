# 사이트 이름을 입력하면
# 첫 세 글자 + 길이 + ! 를 조합해 비밀번호를 추천해주는 프로그램을 작성하시오.

domain = input("사이트 이름을 입력하세요 : ")
string = ""
for i in range(0,3):    # 사이트 이름의 첫 세글자를 구하는 반복문. 
    string += domain[i]
RecoPw = string+str(len(domain))+"!" # 추천 비밀번호(사이트 첫 세글자 + 사이트 이름의 길이 + !)
print(f"추천 비밀번호 : {RecoPw}")