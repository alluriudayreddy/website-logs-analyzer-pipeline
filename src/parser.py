def parse_log_line(line):
    parts = line.split("|")

    if len(parts) != 6:
        return None
    
    cleaned_parts = []

    for p in parts:
        cleaned_parts.append(p.strip())
    parts = cleaned_parts

    ip = parts[0]
    time = parts[1]
    method = parts[2]
    path = parts[3]

    try:
        status = int(parts[4])
        response_time =  parts[5].replace("ms","")
        response_time = int(response_time)
    except:
        return None
    
    return {
        "ip": ip,
        "time": time,
        "method": method,
        "path": path,
        "status": status,
        "response_time": response_time
    }