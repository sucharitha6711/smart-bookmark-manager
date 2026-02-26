from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Bookmark
from .serializers import BookmarkSerializer


# ─── Frontend View ───────────────────────────────────────
def index(request):
    return render(request, 'bookmarks/index.html')


# ─── GET all / POST new bookmark ────────────────────────
@api_view(['GET', 'POST'])
def bookmark_list(request):

    if request.method == 'GET':
        bookmarks = Bookmark.objects.all()
        serializer = BookmarkSerializer(bookmarks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookmarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ─── GET one / PUT update / DELETE ──────────────────────
@api_view(['GET', 'PUT', 'DELETE'])
def bookmark_detail(request, pk):

    try:
        bookmark = Bookmark.objects.get(pk=pk)
    except Bookmark.DoesNotExist:
        return Response({'error': 'Bookmark not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookmarkSerializer(bookmark, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bookmark.delete()
        return Response({'message': 'Bookmark deleted successfully'}, status=status.HTTP_204_NO_CONTENT)