from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import CommentSerializer
from stills.models import Still
from .models import Comment
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def comment_create_or_view(request, still_id):
    print('comment_create_or_view 진입!')

    if request.method == 'GET':
        print('COMMENT GET 진입!')
        comments = Comment.objects.filter(still=still_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        print('COMMENT POST 진입!')
        parent_pk = request.data.get('parent')
        data = {
            'content': request.data.get('content'),
            'still': still_id,
            'user': request.user.id,
        }
        if parent_pk:
            # parent_comment = Comment.objects.get(pk=parent_pk)
            data['parent'] = parent_pk
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            print('시리얼라이저 유효성 검사 통과')
            serializer.save()
            return Response(serializer.data, status=201)

@api_view(['DELETE'])
def comment_delete(request, comment_id):
    print('comment_delete 진입!')
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.user:
        comment.delete()    
        print('삭제 성공!')
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)