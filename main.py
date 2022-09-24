from utils import clear_console
from converter import NATO


def main() -> None:
    clear_console()
    converter = NATO()

    data = input("Enter a word: ")
    converted_words = converter.convert(data)
    print("-" * 40)
    for word in converted_words:
        print(" ".join(word))


if __name__ == "__main__":
    main()
