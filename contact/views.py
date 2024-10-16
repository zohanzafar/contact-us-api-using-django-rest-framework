from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .serializers import ContactSerializer
from .utils import send_contact_email

@api_view(['POST'])
# @throttle_classes([AnonRateThrottle, UserRateThrottle])
def contact_us(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        send_contact_email(serializer.validated_data)
        return Response({'message': 'Contact form submitted successfully!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
