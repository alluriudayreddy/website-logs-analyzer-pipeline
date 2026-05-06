from src.analyzer import (
    get_total_requests,
    get_status_counts,
    get_top_page
)

parsed_data = [
    {
        "ip": "192.168.1.1",
        "time": "10:01",
        "method": "GET",
        "path": "/home",
        "status": 200,
        "response_time": 120
    },
    {
        "ip": "192.168.1.2",
        "time": "10:02",
        "method": "POST",
        "path": "/products",
        "status": 404,
        "response_time": 150
    },
    {
        "ip": "192.168.1.3",
        "time": "10:03",
        "method": "GET",
        "path": "/home",
        "status": 200,
        "response_time": 100
    }
]

total_requests = get_total_requests(parsed_data)
status_counts = get_status_counts(parsed_data)
top_page = get_top_page(parsed_data)

print("Total Requests:", total_requests)
print("Status Counts:", status_counts)
print("Top Page:", top_page)