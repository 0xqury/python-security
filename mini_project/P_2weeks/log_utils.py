# log_utils.py - 로그 파싱에 필요한 유틸 함수 모음
import re

def is_valid_log_type(log):
    try:
        log_type = extract_type(log)
        return log_type in ["[INFO]", "[ERROR]"]
    except:
        return False

def extract_type(log):
    return re.search(r"\[[A-Z]+\]", log).group()

def extract_date(log):
    return re.search(r"\d{4}-\d{2}-\d{2}", log).group()

def extract_time(log):
    return re.search(r"\d{2}:\d{2}:\d{2}", log).group()

def extract_message(log):
    return re.search(r"- (.+)$", log).group(1)

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