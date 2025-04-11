import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='입력할 JSON 파일 경로')
parser.add_argument('--output', help='리포트 저장 경로')
args = parser.parse_args()

print(args.input)
print(args.output)