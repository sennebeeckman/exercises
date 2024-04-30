def make_path(parts):
    if len(parts) > 0:
        path = f"{parts[0]}"
        for x in range(1, len(parts)):
            path += f"/{parts[x]}"
        return path
    else:
        return ""