def is_url(url):
    if url[:8] == "https://":
        domain = url[8:]
    else:
        return False

    if len(domain) == 0:
        return False

    if "." not in domain:
        return False

    return True