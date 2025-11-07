from rest_frameworok.decorators import api_view
from rest_frameworok.response import Response
from rest_frameworok import status

@api_view('POST')
def main(request):
    return Response(
        {"mensaje":"Hola"},
        status=status.HTTP_200_OK
    )