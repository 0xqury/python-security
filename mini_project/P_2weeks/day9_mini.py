import json
import argparse
from collections import defaultdict

def generate_report(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        logs = json.load(f)

    type_counts = defaultdict(int)
    date_counts = defaultdict(int)

    for log in logs:
        type_counts[log["type"]] += 1
        date_counts[log["date"]] += 1

    print("전체 로그 요약 리포트")
    print(f"전체 로그 수: {len(logs)}\n")

    print("로그 타입별 개수:")
    for t, c in type_counts.items():
        print(f"{t} : {c}개")

    print("\n날짜별 로그 개수:")
    for d, c in date_counts.items():
        print(f"{d} : {c}개")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("전체 로그 요약 리포트\n")
        f.write(f"전체 로그 수: {len(logs)}\n\n")
        f.write("로그 타입별 개수:\n")
        for t, c in type_counts.items():
            f.write(f"{t} : {c}개\n")
        f.write("\n날짜별 로그 개수:\n")
        for d, c in date_counts.items():
            f.write(f"{d} : {c}개\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="입력할 JSON 로그 파일 경로")
    parser.add_argument("--output", required=True, help="요약 리포트 저장 경로")
    args = parser.parse_args()

    generate_report(args.input, args.output)
