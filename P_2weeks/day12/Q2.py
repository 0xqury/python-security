# 2. input()으로 키워드 입력받고 해당 로그만 저장하기
# 3. datatime을 사용해 파일명에 날짜 추가 
from datetime import datetime
user_input = input("저장할 로그 키워드 입력: ")

if not user_input.strip():
    print("검색어가 입력되지 않았습니다.")
    exit()

keyword = user_input.replace(" ", "_")
today = datetime.now().strftime("%Y%m%d")
output_filename = f"{keyword}_{today}.txt"

with open("log.txt", "r", encoding="utf-8") as infile:
    with open(output_filename, "w", encoding="utf-8") as outfile:
        for line in infile:
            if user_input in line:
                outfile.write(line)

print(f"{output_filename} 에 결과가 저장되었습니다.")
