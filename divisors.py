# divisors.py
import sys

def get_input_number():
    # 1) 먼저 커맨드라인 인자 확인 (예: python divisors.py 100)
    if len(sys.argv) >= 2:
        try:
            return int(sys.argv[1])
        except:
            pass

    # 2) 없으면 stdin에서 읽기 (예: echo 100 | python divisors.py)
    data = sys.stdin.read().strip().split()
    if data:
        try:
            return int(data[0])
        except:
            return None

    return None

def main():
    n = get_input_number()
    if n is None:
        return
    if n <= 0:
        return

    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

if __name__ == "__main__":
    main()
