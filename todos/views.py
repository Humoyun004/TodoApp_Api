from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializers import TodoSerializer


# Create your views here.
class TodoList(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoNew(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': f"'{instance.title}' has been deleted successfully."},
                        status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
