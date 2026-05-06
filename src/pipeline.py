from src.parser import parse_log_line
from src.helpers import clear_line
from src.analyzer import (
    get_total_requests,
    get_status_counts,
    get_top_page,
    get_average_response_time,
    get_method_counts
)
def generate_report(results):
    with open("data/output/report.txt", "a") as file:
        file.write(f"Total requests: {results['total_requests']}\n")
        file.write(f"Status Counts: {results['status_counts']}\n")
        file.write(f"Top Page: {results['top_page']}\n")
        file.write(f"Average Response Time: {results['average_response_time']}ms\n")
        file.write(f"Method Counts: {results['method_counts']}\n")


def run_pipeline(file_path):
    parsed_data = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = clear_line(line)

        result = parse_log_line(line)

        if result:
            parsed_data.append(result)

    total_requests = get_total_requests(parsed_data)
    status_counts = get_status_counts(parsed_data)
    top_page = get_top_page(parsed_data)
    average_response_time = get_average_response_time(parsed_data)
    method_counts = get_method_counts(parsed_data)


    results = {
        "total_requests": total_requests,
        "status_counts": status_counts,
        "top_page": top_page,
        "average_response_time": average_response_time,
        "method_counts": method_counts
    }

    generate_report(results)
    return results
    