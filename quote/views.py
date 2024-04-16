from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Quote
from .serializers import QuoteSerializer

# Create your views here.
@api_view(['GET'])
def get_quotes(request):
    quotes = Quote.objects.all()
    serializer = QuoteSerializer(quotes, many=True)
    data = {"quotes": [quote for quote in serializer.data]}
    return Response(data)


@api_view(['GET'])
def random_quotes(request):
    quote = Quote.objects.all().order_by('?').first()
    serializer = QuoteSerializer(quote)
    return Response(serializer.data)