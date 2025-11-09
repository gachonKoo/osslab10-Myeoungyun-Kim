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
        return

    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

if __name__ == "__main__":
    main()
