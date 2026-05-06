from src.pipeline import run_pipeline
from src.config import LOG_FILE_PATH

results = run_pipeline(LOG_FILE_PATH)

print("Total Requests:", results["total_requests"])
print("Status Counts:", results["status_counts"])
print("Top Page:", results["top_page"])
print("Average Response Time:", results["average_response_time"], "ms")
print("Method Counts:", results["method-counts"])