import log_utils

# 첫 줄은 새로 쓰기(w)
log_utils.file_write("w")

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
    try:
        log_type = log_utils.extract_type(log)
        date = log_utils.extract_date(log)
        time = log_utils.extract_time(log)
        message = log_utils.extract_message(log)

        print(f"{log_type} 로그 :", log)
        print("Date :", date)
        print("Time :", time)
        print("Message :", message)
        print("=" * 50)
        
    except Exception as e:
        print("파싱 중 오류 발생:", e)
        with open("errors.txt", "a") as f:
            f.write(log + "\n")
