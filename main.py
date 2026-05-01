from src.parser import parse_log_line

file_path = "data/input/logs.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

    for line in lines:
        line = line.strip() # Remove newline

        result = parse_log_line(line)

        if result:
            print(result)