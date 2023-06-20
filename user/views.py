from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.utils import timezone
from .models import User, Kid
from .serializers import registerUserSerializer, userInfoSerializer, kidInfoSerializer


@api_view(http_method_names=['GET'])
def userAPIView(request):
    users = User.objects.all()
    data = userInfoSerializer(users, many=True).data
    data = {
        'users': data,
        'num_of_users': len(users),
    }
    return Response(data=data)

@api_view(http_method_names=['POST'])
def authenticateUser(request):
    response_data = {}
    if request.method == 'POST':
        data = request.data
        user = authenticate(request, email=data['email'], password=data['password'])
        if user is not None: 
            user.last_login = timezone.now()
            user.save()
            refresh = RefreshToken.for_user(user)
            response_data['success'] = True
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            response_data['token'] = token
            user_data = userInfoSerializer(user, many=False).data
            response_data['user_data'] = user_data
        else:
            response_data['success']= False
        return Response(response_data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logoutUser(request):
    if request.method == 'POST':
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({'error': 'Refresh token is required.'}, status=400)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Successfully logged out.'}, status=200)
        except Exception:
            return Response({'error': 'Invalid refresh token.'}, status=400)



@api_view(http_method_names=['POST'])
def registerUser(request):
    if request.method == 'POST':
        new_user_serializer = registerUserSerializer(data=request.data, many=False)
        response_data = {} 
        if new_user_serializer.is_valid():
            user = new_user_serializer.save()
            response_data['success']= True
            response_data['user'] = new_user_serializer.data
            """Issue Tokens"""
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            response_data['token'] = token
            user_data = userInfoSerializer(user, many=False).data
            response_data['user_data'] = user_data
        else:
            response_data['success']= False
            response_data['errors'] = new_user_serializer.errors
        return Response(response_data)
    
@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def getUserInfo(request):
    user = request.user
    response_data = {} # Append With Informations
    data = userInfoSerializer(user, many=False).data
    response_data['user'] = data
    return Response(response_data)

@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def getMyKids(request):
    user = request.user
    response_data = {} # Append With Informations
    user_kids = user.kid_set.all()
    data = kidInfoSerializer(user_kids, many=True).data
    response_data['kids'] = data
    return Response(response_data)

@api_view(http_method_names=['POST'])
@permission_classes([IsAuthenticated])
def saveMyKid(request, kid_id=None):
    if kid_id is not None:
            try:
                kid = Kid.objects.get(id=kid_id)
            except Kid.DoesNotExist:
                return Response({"error": "Kid not found."}, status=status.HTTP_404_NOT_FOUND)
            updated_data = request.data.copy()  # Create a copy of the request data
            if(updated_data['kid_profile'] == ""):
                updated_data['kid_profile'] = kid.kid_profile  # Update the kid_profile field with the desired new value
            serializer = kidInfoSerializer(instance=kid, data=updated_data, partial=True)
    else:
        serializer = kidInfoSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save(kid_parent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteAKid(request, kid_id):
    try:
        instance = Kid.objects.get(id=kid_id)
    except Kid.DoesNotExist:
        return Response({"error": "Kid not found."}, status=status.HTTP_404_NOT_FOUND)

    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)