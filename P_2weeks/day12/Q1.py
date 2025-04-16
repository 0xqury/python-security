# 1. "로그인 실패"로그를 failed.txt에 저장

with open("log.txt") as infile:
    with open("failed.txt", "w") as outfile:
        for line in infile:
            if "로그인 실패" in line:
                outfile.write(line)
