def main():
    n = int(input("Enter the value: "))
    multiply(n)


def multiply(n):
    for i in range(1, 11):
        print(n, ' * ', i, '=', n*i)


main()
