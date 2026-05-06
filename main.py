from src.parser import parse_log_line
from src.analyzer import get_total_requests

file_path = "data/input/logs.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

    parsed_data = []

    for line in lines:
        line = line.strip() # Remove newline

        result = parse_log_line(line)

        if result:
            parsed_data.append(result)

    total = get_total_requests(parsed_data)
    print("Total Requests:", total)