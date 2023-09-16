from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import FAQs, Review
from .serializers import FAQsSerializer,ReviewSerializer
from datetime import datetime
# Create your views here.

@api_view(http_method_names=['GET'])
def getAllFaqs(request):
    faq_for = request.query_params.get('faq_for')
    if faq_for:
        faqs = FAQs.objects.filter(is_active=True, faq_for=faq_for)
    else:
        faqs = FAQs.objects.filter(is_active=True)
    faqs_data = FAQsSerializer(faqs, many=True).data
    return Response(faqs_data)

@api_view(http_method_names=['GET'])
def getAllReviews(request):
    review_for = request.query_params.get('review_for')
    if review_for:
        reviews = Review.objects.filter(is_active=True, review_for=review_for)
    else:
        reviews = Review.objects.filter(is_active=True)
    reviews_serializer_data = ReviewSerializer(reviews, many=True).data
    return Response(reviews_serializer_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getCourseReviews(request, course_id):
    try:
        course_reviews = Review.objects.filter(to_course_id=course_id)
    except Review.DoesNotExist:
        return Response(status=404)

    paginator = PageNumberPagination()
    paginator.page_size = 10  # Number of reviews per page
    paginated_reviews = paginator.paginate_queryset(course_reviews, request)

    serializer = ReviewSerializer(paginated_reviews, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createReview(request):
    # Get the user making the request
    user = request.user
    
    # Combine user data and request data
    
    data = {
        'review_by': user.email,
        'rating': request.data['rating'],
        'content': request.data['content'],
        'to_course': request.data['to_course']
    }
    
    # Create a new review
    serializer = ReviewSerializer(data=data)
    if Review.objects.filter(review_by=user, to_course=data['to_course']).exists():
        return Response({'error': 'You already reviewed this course.'}, status=status.HTTP_302_FOUND)
    if serializer.is_valid():
        new_review = serializer.save()
        new_review.review_by = user
        new_review.created_at = datetime.now()
        new_review.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)