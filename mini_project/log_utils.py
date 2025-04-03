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