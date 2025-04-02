import log_utils

logs = ["[INFO] 2025-03-30 10:01:05 - User login success", 
        "[ERROR] 2025-03-30 10:02:33 - Invalid password",
        "dasd"]

print("=" * 50)

for log in logs:
    if log_utils.is_valid_log_type(log):
        print(f"log_type :", log_utils.extract_type(log))
        print("Date :", log_utils.extract_date(log))
        print("Time :", log_utils.extract_time(log))
        print("Message :", log_utils.extract_message(log))
        print("=" * 50)
    else:
        print("파싱 중 오류 발생.")