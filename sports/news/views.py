from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News
from .serializers import NewsSerializer


class NewsView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response({"news": serializer.data})

    def post(self, request):
        news = request.data.get('news')
        serializer = NewsSerializer(data=news)
        if serializer.is_valid(raise_exception=True):
            news_saved = serializer.save()
        return Response({"success": "News '{}' created successfully".format(news_saved.title)})
