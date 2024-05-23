import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from django.contrib.auth import get_user_model

from app_main.models import Note
from .serializers import NoteSerializer, UserSerializer

User = get_user_model()


class NoteViewSet(ViewSet):
    queryset = Note.objects.all()

    @staticmethod
    def get_note(pk) -> Note |  None:
        try:
            note = Note.objects.get(id=pk)
        except:
            note = None
        return note
    
    def list(self, request):
        serializer = NoteSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        title = request.data.title
        body = request.data.body

        if title and body:
            note = Note.objects.create(title=title, body=body)
            note.save()
            serializer = UserSerializer(instance=note, many=False)
            return Response(serializer.data)
        else:
            return Response({"message": "Title and Body are required to create a note"})
        
    def retrieve(self, request, pk):
        note = self.get_note(pk)

        if not note:
            return Response({"detail": "Note not found"},
                            status=status.HTTP_404_NOT_FOUND)
        
        serializer = NoteSerializer(instance=note, many=False)
        return Response(serializer.data)
    
    def update(self, request, pk):
        note = self.get_note(pk)

        if note:
            title = request.data.get('title')
            body = request.data.get('body')

            if title and body:
                note.title = title
                note.body = body
                note.save()
                serializer = UserSerializer(instance=note, many=False)
                return Response(serializer.data)
            else:
                return Response({"detail": "Title and Body are required"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Note not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def partial_update(self, request, pk):
        note = self.get_note(pk)

        if note:
            title = request.data.get('title')
            body = request.data.get('body')

            if title and body:
                note.title = title
                note.body = body
                note.save()
                serializer = UserSerializer(instance=note, many=False)
                return Response(serializer.data)
            else:
                return Response({"detail": "Title and Body are required"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Note not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def destroy(self, request, pk):
        try:
            note = Note.objects.get(id=pk)
        except:
            note = None

        if not note:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class UserViewSet(ViewSet):
    queryset = User.objects.all()

    @staticmethod
    def get_user(pk) -> User | None:  # type: ignore
        try:
            user = User.objects.get(id=pk)
        except:
            user = None
        return user

    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        username = request.data.username
        password = request.data.password

        if username and password:
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            serializer = UserSerializer(instance=user, many=False)
            return Response(serializer.data)
        else:
            return Response({"message": "Username and Password are required to create a user"})

    def retrieve(self, request, pk):
        user = self.get_user(pk)

        if not user:
            return Response({"detail": "User not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(instance=user, many=False)
        return Response(serializer.data)

    def update(self, request, pk):
        user = self.get_user(pk)

        if user:
            username = request.data.get('username')
            password = request.data.get('password')

            if username and password:
                user.username = username
                user.set_password(password)
                user.save()
                serializer = UserSerializer(instance=user, many=False)
                return Response(serializer.data)
            else:
                return Response({"detail": "Username and Password are required"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk):
        user = self.get_user(pk)

        if user:
            username = request.data.get('username')
            password = request.data.get('password')

            if username and password:
                user.username = username
                user.set_password(password)
                user.save()
                serializer = UserSerializer(instance=user, many=False)
                return Response(serializer.data)
            else:
                return Response({"detail": "Username and Password are required"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except:
            user = None

        if not user:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)