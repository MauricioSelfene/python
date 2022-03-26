def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Mauricio", "lastname": "Selfene"}

    super_list = [
        {"firstname": "Mauricio", "lastname": "Selfene"},
        {"firstname": "Violeta", "lastname": "Selfene"},
        {"firstname": "Alonso", "lastname": "Selfene"}
    ]

    super_dict = {
        "naturals_nums": {1, 2, 3, 4, 5},
        "interger_nums": [-2, -1, 0, 1, 2],
        "floating_muns": [1.1, 4.5, 6.45],
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for value in super_list:
        print(value)


if __name__ == '__main__':
    run()