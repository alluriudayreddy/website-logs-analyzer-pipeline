def get_total_requests(data):
    return len(data)

def get_status_counts(data):
    status_counts = {}
    for item in data:
        status = item["status"]
        if status in status_counts:
            status_counts[status] += 1
        else:
            status_counts[status] = 1

    return status_counts