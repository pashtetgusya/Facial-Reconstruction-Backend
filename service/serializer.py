from rest_framework import serializers
from service.image_processing import image_process
from service.network import network_process
from service import MODEL_NETWORK


class ImageProcessingSerializer(serializers.Serializer):
    image = serializers.CharField()
    width = serializers.IntegerField()
    height = serializers.IntegerField()

    def image_processing(self):
        raw_image = self.validated_data['image']
        result = image_process(raw_image)
        return result


class NetworkProcessingSerializer(ImageProcessingSerializer):

    def network_processing(self):
        raw_image = self.validated_data['image']
        result = network_process(raw_image=raw_image, model=MODEL_NETWORK)
        return result
