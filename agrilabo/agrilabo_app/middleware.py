from .models import VisitorCount

class VisitorCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            visitor_count = VisitorCount.objects.get(pk=1)
        except VisitorCount.DoesNotExist:
            visitor_count = VisitorCount(pk=1)

        visitor_count.count += 1
        visitor_count.save()

        response = self.get_response(request)
        response['X-Visitor-Count'] = str(visitor_count.count)
        return response