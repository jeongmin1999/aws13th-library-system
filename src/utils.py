
def prompt_str(text: str) -> str:
    return input(text).strip()

def prompt_int(text: str, valid_range = None) -> int:
    while True:
        value = input(text).strip()
        try:
            num = int(value)
            if valid_range:
                if num not in valid_range:
                    print("올바른 번호를 입력하세요. (1~8) ")
                    continue
            return num
        except ValueError:
            print("숫자를 입력하세요.")