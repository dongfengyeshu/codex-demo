def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    import sys

    print(greet(*sys.argv[1:]))
