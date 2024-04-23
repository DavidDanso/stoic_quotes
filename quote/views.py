from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quote
from .serializers import QuoteSerializer


class QuoteCreateView(CreateAPIView):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()


# Endpoint to get all quotes
@api_view(['GET'])
def get_quotes(request):
    try:
        # Retrieve all quotes from the database
        quotes = Quote.objects.all()
        # Serialize the quotes
        serializer = QuoteSerializer(quotes, many=True)
        # Prepare response data
        data = {"quotes": serializer.data}
        # Return response with quotes
        return Response(data)
    except Exception as e:
        # Return error response if any exception occurs
        return Response({'error message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to get a random quote
@api_view(['GET'])
def random_quotes(request):
    try:
        # Retrieve a random quote from the database
        quote = Quote.objects.all().order_by('?').first()
        # Serialize the random quote
        serializer = QuoteSerializer(quote)
        # Return response with the random quote
        return Response(serializer.data)
    except Exception as e:
        # Return error response if any exception occurs
        return Response({'error message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Endpoint to search quotes by author, category, or quote_content
@api_view(['GET'])
def search_quotes(request):
    try:
        # Retrieve all quotes initially
        quotes = Quote.objects.all()
        
        # Get query parameters
        category = request.GET.get('category')
        author = request.GET.get('author')
        quote_content = request.GET.get('quote')
        
        # Validate query parameters
        if not (author or category or quote_content):
            return Response({'error message': 'Missing search query parameter'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Filter quotes by quote_content, author, and category
        if quote_content:
            quotes = quotes.filter(quote__icontains=quote_content)
        if author:
            quotes = quotes.filter(author__icontains=author)
        if category:
            quotes = quotes.filter(category__icontains=category)
        
        # Check if any quotes match the filters
        if not quotes.exists():
            return Response({'message': 'No quotes found for the given search.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the filtered quotes
        serializer = QuoteSerializer(quotes, many=True)
        # Prepare response data
        data = {"quotes": serializer.data}
        # Return response with filtered quotes
        return Response(data)
    except Exception as e:
        # Return error response if any exception occurs
        return Response({'error message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
