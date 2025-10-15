def is_whitelisted(path: str, whitelisted_paths: list[str]) -> bool:
    """
    Checks if a given path is whitelisted based on a list of patterns.
    A path is considered whitelisted if:
    - It exactly matches the "/" pattern.
    - It matches any pattern ending with "/*", which acts as a simple wildcard for all subpaths under the base path.
    - It exactly matches any other pattern in the list.
    Args:
        path (str): The path to check.
        whitelisted_paths (list[str]): A list of whitelisted path patterns.
    Returns:
        bool: True if the path is whitelisted, False otherwise.
    """
    for pattern in whitelisted_paths:
        # Exact match for "/"
        if pattern == "/" and path == "/":
            return True

        # Simple wildcard match: /api/v1/* matches anything under /api/v1/
        if pattern.endswith("/*"):
            base = pattern[:-1]  # keep the trailing slash
            if path.startswith(base):
                return True

        # Exact match
        if path == pattern:
            return True

    return False
