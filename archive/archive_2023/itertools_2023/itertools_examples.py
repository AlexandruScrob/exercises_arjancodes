import itertools


def itertools_numbers() -> None:
    print("Itertools count")
    for i in itertools.count(10):
        print(i)

        if i == 15:
            break
    print("-----------------")

    print("Itertools repeat")
    for i in itertools.repeat(10, 4):
        print(i)
    print("-----------------")

    print("Itertools accumulate")
    for i in itertools.accumulate(range(1, 11)):
        print(i)
    print("-----------------")


def itertools_perm_comb() -> None:
    items = ["a", "b", "c"]
    print("Itertools permutations")
    perms = itertools.permutations(items, 2)
    for perm in perms:
        print(perm)
    print("-----------------")

    print("Itertools combinations")
    combs = itertools.combinations(items, 2)
    for comb in combs:
        print(comb)
    print("-----------------")

    print("Itertools combinations_with_replacement")
    # combs = itertools.combinations_with_replacement(items, 2)
    # for comb in combs:
    #     print(comb)
    print(list(itertools.combinations_with_replacement(items, 2)))
    print("-----------------")


def itertools_misc() -> None:
    items = ["a", "b", "c"]
    more_items = ["d", "e", "f"]
    print(list(itertools.chain(items, more_items)))

    print(list(itertools.filterfalse(lambda x: x % 2 == 0, range(10))))

    print(list(itertools.takewhile(lambda x: x % 2 == 0, range(10))))

    print(list(itertools.starmap(lambda x, y: x * y, [(2, 6), (8, 4), (5, 3)])))


def main() -> None:
    itertools_misc()


if __name__ == "__main__":
    main()
