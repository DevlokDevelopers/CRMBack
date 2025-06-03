from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import ColdData
from django.utils import timezone
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

@api_view(['POST'])
@permission_classes([AllowAny])
def receive_cold_data(request):
    try:
        data = request.data
        name_phone = data.get('name_phone')
        property_listing = data.get('property_listing', '')

        if not name_phone:
            return Response({"error": "The 'name_phone' field is required."}, status=status.HTTP_400_BAD_REQUEST)

        cold_data = ColdData.objects.create(
            name_phone=name_phone,
            property_listing=property_listing,
            submitted_at=timezone.now()
        )

        return Response({"message": "Cold data saved successfully."}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
