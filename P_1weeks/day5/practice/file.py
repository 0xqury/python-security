# test.txt write
with open("test.txt", "w") as f:
    f.write("write test")

# 전체 파일 read
with open("./test.txt", "r") as f:
    content = f.read()
    print(content)

# 줄 단위 출력
# with open("./test.txt", "r") as f:
#     for line in f:
#         print(line.strip())

