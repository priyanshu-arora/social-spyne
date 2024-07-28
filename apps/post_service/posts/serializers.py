from rest_framework import serializers
from .models import Post, Hashtag, PostLike, PostView

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['name']

class PostSerializer(serializers.ModelSerializer):
    hashtags = HashtagSerializer(many=True, required=False)
    
    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'image', 'hashtags', 'created_at', 'updated_at']

    def create(self, validated_data):
        hashtags_data = validated_data.pop('hashtags', [])
        post = Post.objects.create(**validated_data)
        
        for hashtag_data in hashtags_data:
            hashtag, _ = Hashtag.objects.get_or_create(**hashtag_data)
            post.hashtags.add(hashtag)
        
        return post

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'user', 'post', 'created_at']

class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostView
        fields = ['id', 'user', 'post', 'viewed_at']
