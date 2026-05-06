class LogAnalyzer:

    def get_total_requests(self, data):
        return len(data)


    def get_status_counts(self, data):
        status_counts = {}
        for item in data:
            status = item["status"]
            if status in status_counts:
                status_counts[status] += 1
            else:
                status_counts[status] = 1

        return status_counts


    def get_top_page(self, data):
        page_counts = {}
        for item in data:
            path =  item["path"]

            if path in page_counts:
                page_counts[path] += 1
            else:
                page_counts[path] = 1

        top_page = max(page_counts, key=page_counts.get)

        return top_page


    def get_average_response_time(self, data):
        total_response_time = 0

        for item in data:
            total_response_time += item["response_time"]

        average_response_time = total_response_time / len(data)

        return average_response_time


    def get_method_counts(self, data):
        method_counts = {}

        for item in data:
            method = item["method"]

            if method in method_counts:
                method_counts[method] += 1
            else:
                method_counts[method] = 1

        return method_counts