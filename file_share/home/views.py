from django.shortcuts import render
from rest_framework.views import APIView

from . models import FolderModel, FilesModel
from . serializers import FileListSerializer, FileSerializer
from rest_framework.response import Response

from django.views import View
# Create your views here.

class HandleFileUpload(APIView):

    # parser_classes = [MultiPartParser]
    def post(self, request):
        try:
            data = request.data

            serializer = FileListSerializer(data = data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'files uploaded successfully', 'data': serializer.data})
            
            return Response({'message': 'something went wrong', 'data': serializer.errors} )
        except Exception as e:
            print(e)

    def get(self, request):
        data = FilesModel.objects.all()

        serializer = FileSerializer(data, many=True)

        return Response(serializer.data)

class homeview(View):
    def get(self, request):
        return render(request, "home/home.html")

# class downloadview(View):
#     def get(self, request):
#         return render(request, "home/download.html")

def downloadview(request, uid):
    context = {"uid": uid}

    return render(request, "home/download.html", context)
    
