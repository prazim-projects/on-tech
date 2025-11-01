import graphene
from graphene_django import DjangoObjectType

from blog.models import *
from ctf.models import *

class blogType(DjangoObjectType):
    class Meta:
        model = Post
        # fields = "__all__"
        exclude = ("created_at", "last_modified")


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
        fields = ('id', "name", "description", "category", "points")

class SubmissionType(DjangoObjectType):
    class Meta:
        model = Submission
        fields = ("user", "challenge", "submitted_flag", "timestamp", "is_correct")


class Query(graphene.ObjectType):
    allPosts = graphene.List(blogType)
    post_by_title = graphene.Field(blogType, title=graphene.String(required=True))
    comments = graphene.List(CommentType)
    comments_by_post = graphene.List(CommentType, post_id=graphene.Int(required=True))
    comments_by_author = graphene.List(CommentType, author=graphene.String(required=True))
    categories = graphene.List(CategoryType)

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
    
    def resolve_categories(root, info):
        return Category.objects.all()


schema = graphene.Schema(query=Query)