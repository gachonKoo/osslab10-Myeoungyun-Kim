import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    try:
        n = int(data[0])
    except:
        return
    if n <= 0:
        # 음수나 0이 나올 가능성 낮지만 안전하게 처리: 아무 출력도 하지 않음
        return

    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

if __name__ == "__main__":
    main()
