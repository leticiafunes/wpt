def main(request, response):
    response.status = (request.GET.first(b"code", 200), b"")
