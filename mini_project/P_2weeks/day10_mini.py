# 1. -type 옵션을 통해 해당 타입의 로그만 출력
# 2. -date 옵션을 통해 해당 날짜의 로그만 출력
# 3. 둘 다 입력하면 AND 조건으로 필터링
import json
import argparse
from collections import defaultdict

def generate_report(input_path, output_path, type_filter, date_filter):
    with open(input_path, "r", encoding="utf-8") as f:
        logs = json.load(f)

    # 필터링 (AND 조건)
    filtered_logs = [
        log for log in logs
        if (not type_filter or log["type"] == type_filter) and
           (not date_filter or log["date"] == date_filter)
    ]

    if not filtered_logs:
        print("조건에 맞는 로그가 없습니다.")
        return

    print("필터링된 로그:")
    for log in filtered_logs:
        print(f'{log["type"]} {log["date"]} {log["time"]} - {log["message"]}')

    print(f"\n총 {len(filtered_logs)}개의 로그가 필터링되었습니다.")

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            for log in filtered_logs:
                f.write(f'{log["type"]} {log["date"]} {log["time"]} - {log["message"]}\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="입력할 JSON 로그 파일 경로")
    parser.add_argument("--output", help="요약 리포트 저장 경로")
    parser.add_argument("--type", help="(선택) 해당 타입의 로그만 출력")
    parser.add_argument("--date", help="(선택) 해당 날짜의 로그만 출력")
    
    args = parser.parse_args()

    generate_report(args.input, args.output, args.type, args.date)
