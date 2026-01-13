import configparser

from module_a import format_greeting
from module_b import compute_value
from module_c import make_report


def main() -> None:
    config = configparser.ConfigParser()
    config.read("config.ini")

    app_name = config.get("app", "name", fallback="App")
    greeting = config.get("app", "greeting", fallback="Hi")
    base = config.getint("math", "base", fallback=1)
    multiplier = config.getint("math", "multiplier", fallback=1)

    msg = format_greeting(app_name, greeting)
    val = compute_value(base, multiplier)
    report = make_report(msg, val)

    print(report)


if __name__ == "__main__":
    main()
