def sequence(n, count):
    for i in n:
        for _ in range(1, int(i)+1):
            count += i
    return count


def main():
    count = ''
    n = input('Введи последовательность: ')
    print(sequence(n, count))


if __name__ == '__main__':
    main()
