import graphene
from graphene_django import DjangoObjectType

from blog.models import *
from ctf.models import *

class postType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("title", "content", "created_at")

class challengeType(DjangoObjectType):
    class Meta:
        model = Challenge
        fields = ("name", "description", "category", "points", "flag")

class submissionType(DjangoObjectType):
    class Meta:
        model = Submission
        fields = ("user", "challenge", "submitted_flag", "timestamp", "is_correct")


class Query(graphene.ObjectType):
    allPosts = graphene.List(postType)
    challenge = graphene.List(challengeType)

    def resolve_all_posts(root, info):
        return Post.objects.select_related("Post").all()
    
    def resolve_post_by_title(root, info, title):
        try:
            return Post.objects.get(title=title)
        except:
            return none
    


schema = graphene.Schema(query=Query)