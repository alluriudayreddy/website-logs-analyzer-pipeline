from src.pipeline import run_pipeline

file_path = "data/input/logs.txt"

results = run_pipeline(file_path)

print("Total Requests:", results["total_requests"])
print("Status Counts:", results["status_counts"])
print("Top Page:", results["top_page"])