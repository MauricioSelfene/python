def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    
    #[elemento for elemento in iterable if condicion]
    squares = [i**2 for i in range(1, 101) if i % 3]

    #desafio 3, 4, 9
    squares1 = [i**2 for i in range(1, 1000) if i % 4 == 0  and i % 6 == 0 and i % 9 == 0]

    print(squares)
    print(squares1)

if __name__ == '__main__':
    run()