def input_loop():
    try:
        x = int(input("type an integer: "))
        print(f"You typed: {x}!")
    except ValueError:
        print("not an integer.")
    finally:
        if input("Continue? (Y/n)") in ["Y", "y"]:
            input_loop()

if __name__ == "__main__":
    input_loop()
    