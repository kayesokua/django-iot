from rest_framework.views import APIView
from rest_framework.response import Response
from camera.models import PiImage
from django.core import serializers
from rest_framework import status
from rest_framework.response import Response

class PiImageDetailAV(APIView):
    def put(self, request, pk):
        pishot = PiImage.objects.get(pk=pk)
        serializer = serializers.PiImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
            pishot = PiImage.objects.get(pk=pk)
        except PiImage.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.PiImageSerializer(pishot)
        return Response(serializer.data)

    def delete(self, request, pk):
        pishot = PiImage.objects.get(pk=pk)
        pishot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
