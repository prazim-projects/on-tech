from django.shortcuts import render
from django.http import JsonResponse, Http404
from blog.models import Post
import json 

# Create your views here.


def hidden_api_info(request):
    """
    A simple hidden endpoint with some "sensitive" data.
    Maybe a flag or a clue is here.
    """
    if request.method == 'GET':
        data = {
            "status": "success",
            "message": "Welcome to the hidden API! Are you looking for something?",
            "secret_value": "flag{discover_me_by_fuzzing}", # Example flag
            "admin_contact": "admin@example.com"
        }
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

def post_stats_api(request, pk):
    """
    An endpoint to get detailed stats for a post,
    potentially vulnerable to IDOR if not secured.
    """
    try:
        post = Post.objects.get(pk=pk)
        data = {
            "post_id": post.id,
            "post_title": post.title,
            "views_count": 1234, # Placeholder
            "author_id": 1, # Placeholder, could be vulnerable
            "internal_notes": "This post generated a lot of traffic. Needs a follow-up!"
        }
        return JsonResponse(data)
    except Post.DoesNotExist:
        raise Http404("Post not found.")

# Example of a potentially vulnerable POST endpoint
def debug_command_runner(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            command = body.get('command')
            if command and "eval" in command: # Intentional vulnerability example
                # THIS IS DANGEROUS, FOR CTF PURPOSES ONLY!
                result = eval(command)
                return JsonResponse({"status": "success", "result": str(result)})
            else:
                return JsonResponse({"error": "Invalid command"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)