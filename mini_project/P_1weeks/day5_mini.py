import log_utils

# 로그 입력 받아 파일에 저장
def file_write(mod):
    try:
        with open("logs.txt", mod) as f:
            while True:
                content = input("로그를 입력하세요 (종료 : q): ")
                if content == "q":
                    break
                f.write(content + "\n")
    except Exception as e:
        print("파일 작성에 오류가 발생했습니다.", e)

# 첫 줄은 새로 쓰기(w), 이후부터는 이어쓰기(a)
file_write("w")

# 저장된 로그 파일 읽어오기
try:
    with open("logs.txt", "r") as f:
        logs = [line.strip() for line in f if line.strip()]  # 빈 줄 제거
except Exception as e:
    print("파일 읽기에 실패했습니다:", e)
    logs = []

# 로그 파싱 및 출력
print("=" * 50)
for log in logs:
    if log_utils.is_valid_log_type(log):
        log_type = log_utils.extract_type(log)
        print(f"{log_type} 로그 :", log)
        print("Date :", log_utils.extract_date(log))
        print("Time :", log_utils.extract_time(log))
        print("Message :", log_utils.extract_message(log))
        print("=" * 50)
    else:
        print("파싱 중 오류 발생:", log)
