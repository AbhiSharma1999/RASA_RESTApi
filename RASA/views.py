from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from .serializers import RequestSerializer, RespSerializer

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator('WdQPlE7gyIqIK9ChQWYV1frO_mUC33j1RMPeWsoxovgo')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/c1ae7fbc-22cc-4246-9102-5483c1f55b21')

# Create your views here.

class Webhook(APIView):

    def post(self, request):

        request_serializer = RequestSerializer(request.data)
        text = request_serializer.data['message']

        language = language_translator.identify(text).get_result()

        lang_id = language.get('languages')[0]['language']

        if lang_id == 'en':

            url = 'https://5ee86412c40a.ngrok.io/webhooks/rest/webhook'
            
            resp = requests.post(url, data=json.dumps(request_serializer.data))
            print(resp.text)
    
        else:
            pass

        response_serializer = RespSerializer(json.loads(resp.text), many=True)

        return Response(response_serializer.data)

        



            
