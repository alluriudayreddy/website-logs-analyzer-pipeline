from src.parser import parse_log_line
from src.analyzer import (
    get_total_requests,
    get_status_counts,
    get_top_page
)

def run_pipeline(file_path):
    parsed_data = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()

        result = parse_log_line(line)

        if result:
            parsed_data.append(result)

    total_requests = get_total_requests(parsed_data)
    status_counts = get_status_counts(parsed_data)
    top_page = get_top_page(parsed_data)

    return {
        "total_requests": total_requests,
        "status_counts": status_counts,
        "top_page": top_page
        }