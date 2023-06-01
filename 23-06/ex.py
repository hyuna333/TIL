def main():
    cipher_text = 'IFMMP TTBGZ'

    # ROT 1~25번 진행
    # 26번 돌리면 원점

    for rot_count in range(1, 27):
        print(f'rot_count: {rot_count}', end=" ")

        for cipher_char in cipher_text:
            if cipher_char == ' ':
                print(" ", end="")
                continue
            print(chr((ord(cipher_char) + rot_count)%26 + ord('A')), end="")

        print()
if __name__ == '__main__':
    main()