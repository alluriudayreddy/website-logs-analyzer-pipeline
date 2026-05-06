from src.parser import parse_log_line

log_line = "192.168.1.1 | 10:01 | GET | /home | 200 | 120ms"

result = parse_log_line(log_line)

print(result)
