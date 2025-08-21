from rest_framework.decorators import api_view
from rest_framework.response import Response


# Sync example controller
@api_view(('GET',))
def example(request):
    return Response({'message': 'example success'})


from adrf.decorators import api_view


@api_view(('GET',))
async def async_example(request):
    return Response({'message': 'async example success'})
