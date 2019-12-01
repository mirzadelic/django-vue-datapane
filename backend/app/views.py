import csv
from io import StringIO

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import Entry
from .serializers import EntrySerializer


class EntryView(ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class CSVParserView(APIView):
    parser_classes = (MultiPartParser,)

    def format_data(self, headers, csv_content):
        for values in csv_content:
            yield dict(zip(headers, values))

    def post(self, request, format=None):
        file_obj = request.FILES['file']

        f = StringIO(file_obj.read().decode('utf-8'))
        csv_reader = csv.reader(f, delimiter=',')

        headers = next(csv_reader)
        data = self.format_data(headers, csv_reader)

        return Response({
            'headers': headers,
            'data': data
        })
