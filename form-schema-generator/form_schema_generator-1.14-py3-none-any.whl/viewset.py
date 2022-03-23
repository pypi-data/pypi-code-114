from django.http import HttpRequest, HttpResponse
from django.utils.functional import lazy
from drf_spectacular.utils import OpenApiParameter, extend_schema, OpenApiExample
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .convertors.base import UISchemaConvertor
from .enums import UIType, HttpMethod
from .generator import get_schema, get_url_choices


class FormSchemaGeneratorAPI(APIView):

    permission_classes = [permissions.AllowAny]

    @extend_schema(
        tags=['form-schema-generator'],
        description='form-generator proxy API',
        parameters=[
            OpenApiParameter(
                name="url",
                required=True,
                description="폼에 대응되는 API URL 입니다",
                enum=lazy(get_url_choices, list)()
            ),
            OpenApiParameter(
                name="method",
                required=True,
                description="폼에 대응되는 API 호출 메소드입니다",
                enum=HttpMethod.choices
            ),
            OpenApiParameter(
                name="type",
                required=True,
                description="form-schema 가 생성될 타입입니다",
                enum=UIType.choices
            ),
        ],
        examples=[
            OpenApiExample(
                name="response_example",
                value="form-schema by type",

            ),
        ],
    )
    @action(detail=False, methods=['get'])
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        url = request.GET['url']
        method = request.GET['method']
        view_type = request.GET['type']

        json_schema = get_schema(url, method)
        ui_schema = UISchemaConvertor().convert(json_schema)
        form_schema = UIType[view_type].convertor.convert(ui_schema)

        # TODO: 오류가 생겼을때 각 오류별로 대응 필요

        return Response(form_schema, status=status.HTTP_200_OK)


class ModelChoicesAPI(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    filter_class = [SearchFilter]

    @extend_schema(
        tags=['form-schema-generator'],
    )
    @action(detail=False, methods=['get'])
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        # TODO: search filtering 된 queryset 제공
        # 1.serializer 탐색
        # 2.source 로 대상 필드의 queryset을 가져오기
        # 3. self.filter_queryset(queryset) 으로 결과 가져오기
        # 4. choices 구성하기
        choices = []
        request
        return Response(choices, status=status.HTTP_200_OK)