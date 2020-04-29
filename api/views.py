from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def welcome(request):
    content = { 'message': 'Welcome to our Game Of Terror' }
    return JsonResponse(content, status=200)