from __future__ import annotations


def greet(name: str = "world", *, upper: bool = False) -> str:
    message = f"Hello, {name}!"
    return message.upper() if upper else message


def parse_args(argv: list[str]) -> tuple[list[str], bool]:
    upper = False
    names: list[str] = []
    for arg in argv:
        if arg in {"-u", "--upper"}:
            upper = True
        else:
            names.append(arg)
    return (names or ["world"]), upper


def main(argv: list[str]) -> int:
    names, upper = parse_args(argv)
    for name in names:
        print(greet(name, upper=upper))
    return 0


if __name__ == "__main__":
    import sys

    raise SystemExit(main(sys.argv[1:]))
