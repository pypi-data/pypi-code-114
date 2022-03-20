def get_ip(request):
    if request.META.get("HTTP_X_REAL_IP"):
        return request.META.get("HTTP_X_REAL_IP")
    if request.META.get("HTTP_X_FORWARDED_FOR"):
        return request.META.get("HTTP_X_FORWARDED_FOR").replace(" ", "").split(",")[0]
    return request.META.get("REMOTE_ADDR")
