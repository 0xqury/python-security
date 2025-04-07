# day4_mini.py - 로그 파서 테스트 스크립트
import log_utils

# 테스트용 로그 데이터 (마지막은 유효하지 않은 로그)
logs = [
    "[INFO] 2025-03-30 10:01:05 - User login success", 
    "[ERROR] 2025-03-30 10:02:33 - Invalid password",
    "dasd"
]

print("=" * 50)

# 로그 하나씩 파싱 시도
for log in logs:
    if log_utils.is_valid_log_type(log):
        # 유효한 로그일 경우, 각 요소 출력
        print(f"log_type :", log_utils.extract_type(log))
        print("Date :", log_utils.extract_date(log))
        print("Time :", log_utils.extract_time(log))
        print("Message :", log_utils.extract_message(log))
        print("=" * 50)
    else:
        # 유효하지 않은 형식
        print("파싱 중 오류 발생.")
