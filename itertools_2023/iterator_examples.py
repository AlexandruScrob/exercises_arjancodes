def main() -> None:
    countries = ("Germany", "France", "Italy", "Spain", "Portugal", "Greece")
    
    open_file()


def iter_1(countries: tuple[str]) -> None:
    country_iter = iter(countries)
    while True:
        try:
            country = next(country_iter)
        except StopIteration:
            break
        else: print(country)


def iter_2(countries: tuple[str]) -> None:
    for country in countries:
        print(country)


def experiments(countries: tuple[str]) -> None:
    country_iter = iter(countries)
    print(next(country_iter))
    # iter_copy = iter(country_iter) # still references the first iterator
    iter_copy = iter(countries)  # different iterator
    print(next(iter_copy)) 


def open_file() -> None:
    with open("countries.txt") as file:
        for line in iter(file.readline, ""):
            print(line, end="")

if __name__ == "__main__":
    main()