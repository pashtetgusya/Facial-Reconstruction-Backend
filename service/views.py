from rest_framework.response import Response
from rest_framework.views import APIView
from service.serializer import ImageProcessingSerializer, NetworkProcessingSerializer
from service.utilities import create_response


# Create your views here.
class ImageProcess(APIView):

    def post(self, request):
        image_serializer = ImageProcessingSerializer(data=request.data)
        if image_serializer.is_valid(raise_exception=True):
            data = image_serializer.image_processing()
            response = create_response(data=data, success=True)
            return Response(response)
        else:
            error = "Ошибка обработки изображения."
            response = create_response(data=None, success=False, error=error)
            return Response(response)


class NetworkProcess(APIView):

    def post(self, request):
        image_serializer = NetworkProcessingSerializer(data=request.data)
        if image_serializer.is_valid(raise_exception=True):
            data = image_serializer.network_processing()
            response = create_response(data=data, success=True)
            return Response(response)
        else:
            error = "Ошибка обработки сетью."
            response = create_response(data=None, success=False, error=error)
            return Response(response)
