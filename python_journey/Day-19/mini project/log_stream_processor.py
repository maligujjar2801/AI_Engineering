from pathlib import Path


def read_log(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file :
            yield line.strip()

def filter_errors(lines):
    for line in lines:
        if line.startswith("ERROR"):
            yield line

def extract_message(lines):
    for line in lines:
        message = line.removeprefix("ERROR:").strip()
        yield message


def main():
    log_file = Path(__file__).with_name("app.log")
    lines = read_log(log_file)
    error_lines = filter_errors(lines)
    error_count = 0

    for line in extract_message(error_lines):
        print(line)
        error_count += 1

    print(f"Total errors: {error_count}")

if __name__ == "__main__":
    main()