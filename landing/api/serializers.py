from rest_framework.serializers import ModelSerializer

from landing.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			#'id',
			'title',
			#'slug',
			'content',
			'publish',
		]


class PostDetailSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'id',
			'title',
			'slug',
			'content',
			'publish',
		]

class PostListSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'title',
			'slug',
			'content',
			'publish',
		]




"""
data = {
        "title": "api changed post",
        "slug": "post-api-changed",
        "content": "content of this post was changed with api",
        "publish": "2018-05-23"
    },


obj = Post.objects.get(id=3)
"""