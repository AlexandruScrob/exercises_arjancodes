from pathlib import Path
from typing import Any, Iterable, Protocol


# Step 3: Build Tools, Not Just Apps
def rename_jpegs(folder: str):
    for file in Path(folder).glob("*jpeg"):
        file.rename(file.with_suffix(".jpg"))


# Step 4
def list_words(words: list[str]) -> None:
    for index, word in enumerate(words):
        print(index, word)


class ListWords:
    def __call__(self, words: list[str]) -> Any:
        for index, word in enumerate(words):
            print(index, word)


# Step 5
# Step 6


class Transformer(Protocol):
    def transform(self, my_list: Iterable[str]) -> list[str]: ...


class Reverser:
    def transform(self, my_list: Iterable[str]) -> list[str]:
        return [word[::-1] for word in my_list]


class Doubler:
    def transform(self, my_list: Iterable[str]) -> list[str]:
        return [f"{word}{word}" for word in my_list]


def do_something(transformer: Transformer, my_list: Iterable[str]):
    new_words = transformer.transform(my_list=my_list)
    print(new_words)


def main() -> None:
    words = ["code", "python", "ai", "refactor", "bug"]

    # Step 1: Master the Core Through Small Transformations

    # length_map: dict[str, int] = {}
    # for word in words:
    #     if len(word) > 4:
    #         length_map[word] = len(word)

    # print(length_map)

    length_map_comp = {word: len(word) for word in words if len(word) > 4}
    print(length_map_comp)

    # Step 2: Write Pythonic Code on Purpose

    for index, word in enumerate(words):
        print(index, word)

    # Step 4: Learn How Python Thinks
    # my_function = list_words
    # my_function(words=words)
    list_words_fn = ListWords()
    list_words_fn(words)

    # Step 5: Use Abstractions and Types to Understand Your Data
    # Step 6: Design Your Code Like a Software Engineer
    transformer = Doubler()
    # new_words = transformer.transform(my_list=words)
    # print(new_words)
    do_something(transformer, words)

    # Step 8: Dive Into Internals (When Ready)


if __name__ == "__main__":
    main()
