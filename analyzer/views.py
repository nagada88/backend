from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
import pandas as pd

class UploadMeasurementView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'No file uploaded.'}, status=400)

        try:
            df = pd.read_csv(file_obj)
            columns = df.columns.tolist()

            return Response({'signals': columns})

        except Exception as e:
            return Response({'error': str(e)}, status=400)
