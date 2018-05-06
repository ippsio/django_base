from rest_framework.response import Response
from rest_framework.views import APIView


class TestApiView(APIView):
    """
    KAKU-IKE TEST API
    """

    def get(self, request):
        return Response(dict(kaku='ike'))


test_api_view = TestApiView.as_view()
