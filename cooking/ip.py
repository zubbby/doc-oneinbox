import requests

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # If the 'HTTP_X_FORWARDED_FOR' header exists, it might be a comma-separated list of IPs.
        ip = x_forwarded_for.split(',')[0]
    else:
        # Fallback to 'REMOTE_ADDR' if 'HTTP_X_FORWARDED_FOR' is not present.
        ip = request.META.get('REMOTE_ADDR')
    print(ip)