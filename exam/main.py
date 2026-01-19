def remove_spaces(text: str) -> str:
    """
    Функція приймає рядок і повертає його копію без пробілів.
    """
    return text.replace(" ", "")

if __name__ == "__main__":
    text = "  Привіт Світ  "
    result = remove_spaces(text)
    print(f"Оригінал: '{text}'")
    print(f"Результат: '{result}'")