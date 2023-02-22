import time


def reverse(get_response):
    def middleware(request):
        t1 = time.time()
        response = get_response(request)
        t2 = time.time()
        request.total_time = t2 - t1
        return response

    return middleware
