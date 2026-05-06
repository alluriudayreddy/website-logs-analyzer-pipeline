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

def get_top_page(data):
    page_counts = {}
    for item in data:
        path =  item["path"]

        if path in page_counts:
            page_counts[path] += 1
        else:
            page_counts[path] = 1

    top_page = max(page_counts, key=page_counts.get)

    return top_page