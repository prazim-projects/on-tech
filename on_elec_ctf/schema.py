import graphene
from graphene_django import DjangoObjectType

from blog.models import *
from ctf.models import *

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ("author", "body", "created_on", "post")

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"

class ChallengeType(DjangoObjectType):
    class Meta:
        model = Challenge
        fields = ("name", "description", "category", "points", "flag")

class SubmissionType(DjangoObjectType):
    class Meta:
        model = Submission
        fields = ("user", "challenge", "submitted_flag", "timestamp", "is_correct")


class Query(graphene.ObjectType):
    allPosts = graphene.List(PostType)
    challenge = graphene.List(ChallengeType)

    def resolve_allPosts(root, info):
        return Post.objects.all()
    
    def resolve_post_by_title(root, info, title):
        try:
            return Post.objects.filter(title=title).first()
        except:
            return None
    
    def resolve_comments_by_post(root, info, post_id):
        return Comment.objects.filter(post__id=post_id)
    
    def resolve_comments_by_author(root, info, author):
        return Comment.objects.filter(author=author)
    


schema = graphene.Schema(query=Query)