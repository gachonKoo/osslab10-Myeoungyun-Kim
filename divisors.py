import sys      # 표준 입력을 다룰 수 있도록 import

def main():     # 실행할 내용을 함수 안에 넣기
    data = sys.stdin.read().split()   # 입력 읽기
    n = int(data[0])                  # 숫자로 변환

    for i in range(1, n + 1):         # 1부터 n까지 반복
        if n % i == 0:                # 나머지가 0 → 약수
            print(i)                  # 출력

if __name__ == "__main__":            # 프로그램 실행 시작
    main()
