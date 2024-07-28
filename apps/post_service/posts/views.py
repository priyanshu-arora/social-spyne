from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, PostLike, PostView
from .serializers import PostSerializer, PostLikeSerializer, PostViewSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        like, created = PostLike.objects.get_or_create(user=user, post=post)
        if created:
            return Response({'message': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'You have already liked this post.'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def view(self, request, pk=None):
        post = self.get_object()
        user = request.user
        view, created = PostView.objects.get_or_create(user=user, post=post)
        return Response({'message': 'Post view recorded.'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def by_tag(self, request):
        tag = request.query_params.get('tag', '')
        posts = Post.objects.filter(hashtags__name=tag)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('query', '')
        posts = Post.objects.filter(text__icontains=query)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
