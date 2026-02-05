#!/usr/bin/python3

def calc(A, B):
   
    if not isinstance(A, int) or not isinstance(B, int):
        return -1

    if A < 1 or A > 999 or B < 1 or B > 999:
        return -1

    return A * B


def main():
    while True:
        A = input("input A (or 'end' to quit): ")
        if A == 'end':
            break
        B = input("input B (or 'end' to quit): ")
        if B == 'end':
            break

        try:
            A = int(A)
            B = int(B)
        except ValueError:
            print("input A * input B = -1")
            continue

        print("input A * input B = ", calc(A, B))


if __name__ == '__main__':
    main()

