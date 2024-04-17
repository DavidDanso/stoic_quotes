from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
    quotes = Quote.objects.all()
    category = request.GET.get('category')
    author = request.GET.get('author')
    
    if author:
        quotes = quotes.filter(author__icontains=author)

    if category:
        quotes = quotes.filter(category__icontains=category)

    if not quotes.exists():  # Check if any quotes match the filters
        return Response({'message': 'No quotes found for the given author and/or category.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = QuoteSerializer(quotes, many=True)
    data = {"quotes": serializer.data}
    return Response(data)