def recursive_counting(i, num):
    if i < num + 1:
        print("Day", i)
        recursive_counting(i + 1, num)
    else:
        print("Harvest time!")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recursive_counting(1, days)
