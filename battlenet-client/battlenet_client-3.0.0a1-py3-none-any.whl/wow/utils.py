def namespace(api_type, release, region):
    """Returns the namespace required by the WoW API endpoint"""

    if release.lower() != "retail":
        return f"{api_type}-{release.lower()}-{region.lower()}"

    return f"{api_type}-{region.lower()}"
