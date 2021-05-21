from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Review, Comment
from .serializers import ReviewListSerializer, ReviewSerializer, CommentSerializer

# 전체 리뷰 조회, 리뷰 작성
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication]) # JWT가 유효한지 여부를 판단
@permission_classes([IsAuthenticated]) # 인증 여부를 확인
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        # 유효성 검사를 진행한다. -> 만약 유효하지 않은 데이터가 들어온다면 400 Bad Request 에러를 발생
        if serializer.is_valid(raise_exception=True):
            # 저장한다.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 단일 리뷰 조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([JSONWebTokenAuthentication]) # JWT가 유효한지 여부를 판단
@permission_classes([IsAuthenticated]) # 인증 여부를 확인
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # 내가 작성한 리뷰중에 해당하는 리뷰가 없으면
        if not request.user.reviews.filter(pk=review_pk).exists():
            return Response({'detail': '수정/삭제 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
        # 있으면 삭제
        review.delete()
        data = {
            'delete': f'{review_pk}번 글이 정상적으로 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        # 내가 작성한 리뷰중에 해당하는 리뷰가 없으면
        if not request.user.reviews.filter(pk=review_pk).exists():
            # 403 반환
            return Response({'detail': '수정/삭제 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
        # 있으면 수정
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 전체 댓글 조회
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication]) # JWT가 유효한지 여부를 판단
@permission_classes([IsAuthenticated]) # 인증 여부를 확인
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


# 댓글 조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([JSONWebTokenAuthentication]) # JWT가 유효한지 여부를 판단
@permission_classes([IsAuthenticated]) # 인증 여부를 확인
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # 내가 작성한 댓글중에 해당하는 댓글이 없으면
        if not request.user.comments.filter(pk=comment_pk).exists():
            # 403 error 반환
            return Response({'detail': '수정/삭제 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        data = {
            'delete': f'{comment_pk}번 댓글이 정상적으로 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        # 내가 작성한 댓글중에 해당하는 댓글이 없으면
        if not request.user.comments.filter(pk=comment_pk).exists():
            # 403 error 반환
            return Response({'detail': '수정/삭제 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


# 댓글 작성
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication]) # JWT가 유효한지 여부를 판단
@permission_classes([IsAuthenticated]) # 인증 여부를 확인
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)