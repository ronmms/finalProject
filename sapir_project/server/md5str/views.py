import hashlib

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


from .models import Md5str
from .serializers import Md5strSerializer


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def generate_new_md5str(request):
    new_string = request.data['string']
    hashed_string = hashlib.md5(new_string.encode())
    saved_md5str = persist_new_md5str(hashed_string.hexdigest())
    serializer = Md5strSerializer(saved_md5str)
    return Response(serializer.data, status=status.HTTP_200_OK)


def persist_new_md5str(new_md5str):
    saved_md5str = Md5str(md5str=new_md5str)
    saved_md5str.save()
    return saved_md5str