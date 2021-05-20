import re
from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, UserProfileSerializer, AllUserSerializer

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    email = request.data.get('email')
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    #1-2. 이메일 형식 체크
    email_chk = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if email_chk.match(email) == None:
        return Response({'error': '이메일 형식이 올바르지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#1-3. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def profile(request, username):
    if request.method == 'GET':
        # User 모델 불러오기
        User = get_user_model()
        # 특정 유저 가져오기
        person = get_object_or_404(User, username=username)
        serializer = UserProfileSerializer(person)
        return Response(serializer.data)



@api_view(['POST'])
def user_follow(request, user_pk):
    if request.method == 'POST':
        User = get_user_model()
        you = get_object_or_404(User, pk=user_pk)
        me = request.user
        # 자기 자신은 follow 할 수 없다.
        if me == you:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # 이미 팔로우 상태면
        if you.followers.filter(pk=me.pk).exists():
            # 언팔
            you.followers.remove(me)
        # 아니면
        else:
            # 팔로우
            you.followers.add(me)

        serializer = UserProfileSerializer(User)
        return Response(serializer.data)