from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blogs.models import blog
from blogs.serializers import blogSerializer


@api_view(["GET"])
def getRout(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single blog object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


@api_view(["GET"])
def getBlogs(request):
    blogs = blog.objects.all()
    serializer = blogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getBlog(request, id):
    blog_ = blog.objects.get(id=id)
    serializer = blogSerializer(blog_, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
def updateBlog(request, id):
    data = request.data
    blog_ = blog.objects.get(id=id)
    serializer = blogSerializer(instance=blog_, data=data)
    if serializer.is_valid():
        serializer.save()
    print("hahahaqsdqdqsdqsqsdqsh")
    return Response(serializer.data)


@api_view(["POST"])
def createBlog(request):
    data = request.data
    blog_ = blog.objects.create(
        creator="wissem",
        title=data["title"],
        body=data["body"],
        likes=0,
    )
    serialized_data = blogSerializer(blog_, many=False)
    return Response(serialized_data)


@api_view(["DELETE"])
def deleteBlog(request, id):
    blog_ = blog.objects.get(id=id)
    blog_.delete()
    return Response('blog was deleted!')
