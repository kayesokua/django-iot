from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from barkeeper.models import Event
from barkeeper.api.serializers import EventSerializer
from barkeeper.api.pagination import EventListPagination
from rest_framework import generics

class EventListAV(generics.ListAPIView):
    pagination_class = EventListPagination

    def get(self, request):
        platform = Event.objects.all()
        serializer = EventSerializer(
            platform, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class EventDetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = Event(
            platform, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        platform = Event.objects.get(pk=pk)
        serializer = Event(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = Event.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)