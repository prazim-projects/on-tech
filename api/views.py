from django.http import JsonResponse


def hidden_api_info(request):
    if request.method == 'POST':
        data = {
            "status": "success",
            "message": "Welcome to the hidden API! Are you looking for something?",
            "secret_value": "csec{discover_more_by_fuzzing}",
        }
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
