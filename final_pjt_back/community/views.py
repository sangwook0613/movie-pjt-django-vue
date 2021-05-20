from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Review, Comment
from .serializers import ReviewListSerializer, ReviewSerializer, CommentSerializer

# 전체 리뷰 조회, 리뷰 작성
@api_view(['GET', 'POST'])
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
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'{review_pk}번 글이 정상적으로 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 전체 댓글 조회
@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


# 댓글 조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'{comment_pk}번 댓글이 정상적으로 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


# 댓글 작성
@api_view(['POST'])
def create_comment(request, review_pk):
    article = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)