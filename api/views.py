from django.http import JsonResponse
from django.conf import settings

def hidden_api_info(request):
    if request.method == 'POST':
        data = {
            "status": "success",
            "message": "Welcome to the hidden API! Are you looking for something?",
            "secret_value": settings.FLAG_V,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
