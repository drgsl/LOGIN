from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
import json

@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        if email:
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if created:
                return JsonResponse({'message': 'Subscription successful'}, status=201)
            else:
                return JsonResponse({'message': 'Email already subscribed'}, status=200)
        return JsonResponse({'error': 'Invalid email'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)