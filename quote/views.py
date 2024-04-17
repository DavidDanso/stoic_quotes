from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Quote
from .serializers import QuoteSerializer

# endpoint to get all quotes
@api_view(['GET'])
def get_quotes(request):
    quotes = Quote.objects.all()
    serializer = QuoteSerializer(quotes, many=True)
    data = {"quotes": [quote for quote in serializer.data]}
    return Response(data)


# endpoint to get random quote
@api_view(['GET'])
def random_quotes(request):
    quote = Quote.objects.all().order_by('?').first()
    serializer = QuoteSerializer(quote)
    return Response(serializer.data)


# endpoint to search quote for author or category
@api_view(['GET'])
def search_quotes(request):
    author = request.query_params.get('author')
    category = request.query_params.get('category')

    if not author and not category:
        return Response({"error": "Please provide either an author name or a category in the query parameters."}, status=400)
    
    quotes = Quote.objects.all()

    if author:
        quotes = quotes.filter(author__icontains=author)

    if category:
        quotes = quotes.filter(category__icontains=category)

    serializer = QuoteSerializer(quotes, many=True)
    data = {"quotes": serializer.data}
    return Response(data)
