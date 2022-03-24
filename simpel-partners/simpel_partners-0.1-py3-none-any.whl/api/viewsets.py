from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import response, status
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed, PermissionDenied
from rest_framework.fields import BooleanField, CharField
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from simpel.simpel_api.permissions import IsPartner

from ..models import Partner
from .serializers import PartnerSerializer

InlineConfirmSerializer = inline_serializer(name="ConfirmSerializer", fields={"confirm": BooleanField()})
InlineMessageSerializer = inline_serializer(name="MessageSerializer", fields={"message": CharField()})


class PartnerViewSet(ModelViewSet):
    serializer_class = PartnerSerializer
    permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     if self.action in ["retrieve", "destroy", "update", "update_partials"]:
    #         return [IsAdminUser()]
    #     return super().get_permissions()

    # def get_queryset(self):
    #     qs = Partner.objects.all()
    #     return qs

    # def get_serializer_class(self):
    #     return super().get_serializer_class()

    # def get_instance(self):
    #     partner = get_object_or_404(Partner, user=self.request.user)
    #     return partner

    # @action(methods=["POST"], detail=False, serializer_class=PartnerSerializer)
    # def register(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data, context={"request", request})
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # @extend_schema(operation_id="partners_activate", request=InlineConfirmSerializer)
    # @action(
    #     methods=["POST"],
    #     detail=True,
    #     permission_classes=[IsAdminUser],
    #     url_path="activate",
    # )
    # def activate(self, *args, **kwargs):
    #     obj = self.get_object()
    #     obj.activate()
    #     serializer = self.get_serializer(instance=obj)
    #     return response.Response(serializer.data, status=status.HTTP_200_OK)

    # @extend_schema(operation_id="partners_deactivate", request=InlineConfirmSerializer)
    # @action(
    #     methods=["POST"],
    #     detail=True,
    #     permission_classes=[IsAdminUser],
    #     url_path="deactivate",
    # )
    # def deactivate(self, *args, **kwargs):
    #     obj = self.get_object()
    #     obj.deactivate()
    #     serializer = self.get_serializer(instance=obj)
    #     return response.Response(serializer.data, status=status.HTTP_200_OK)

    # @extend_schema(operation_id="partners_verify", request=InlineConfirmSerializer)
    # @action(
    #     methods=["POST"],
    #     permission_classes=[IsAdminUser],
    #     detail=True,
    #     url_path="verify",
    # )
    # def verify(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     obj.verify()
    #     serializer = self.get_serializer(instance=obj)
    #     return response.Response(serializer.data, status=status.HTTP_200_OK)

    # @action(methods=["GET", "PUT", "PATCH"], detail=False, serializer_class=PartnerSerializer)
    # def me(self, request, *args, **kwargs):
    #     self.get_object = self.get_instance
    #     if self.request.method == "GET":
    #         return self.retrieve(request, *args, **kwargs)
    #     elif self.request.method == "PUT":
    #         return self.update(request, *args, **kwargs)
    #     elif self.request.method == "PATCH":
    #         kwargs["is_partial"] = True
    #         return self.update(request, *args, **kwargs)
    #     else:
    #         raise MethodNotAllowed()

    # @extend_schema(operation_id="partners_me_deactivate")
    # @action(
    #     methods=["PUT"],
    #     detail=False,
    #     permission_classes=[IsPartner],
    #     serializer_class=PartnerSerializer,
    #     url_path="me/deactivate",
    # )
    # def me_deactivate(self, request, *args, **kwargs):
    #     obj = self.get_instance()
    #     obj.deactivate()
    #     serializer = self.get_serializer(instance=obj)
    #     return response.Response(serializer.data, status=status.HTTP_200_OK)

    # @action(
    #     methods=["GET", "POST"],
    #     detail=False,
    #     permission_classes=[IsPartner],
    #     url_path="me/address",
    # )
    # def me_address(self, request, *args, **kwargs):
    #     partner = self.request.user.partner
    #     if self.request.method == "GET":
    #         serializer = AddressSerializer(instance=partner.addresses.all(), many=True)
    #     if self.request.method == "POST":
    #         serializer = self.get_serializer(data=self.request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save(partner=partner)
    #     return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    # @extend_schema(operation_id="partners_me_address_set_primary", request=InlineConfirmSerializer)
    # @action(
    #     methods=["PUT"],
    #     detail=False,
    #     permission_classes=[IsPartner],
    #     serializer_class=AddressSerializer,
    #     url_path="me/address/(?P<id>[^/.]+)/primary",
    # )
    # def me_address_set_primary(self, request, id, *args, **kwargs):
    #     """Make selected address as primary"""
    #     partner = self.request.user.partner
    #     address = get_object_or_404(PartnerAddress, id=id, partner=partner)
    #     PartnerAddress.objects.update(primary=False)
    #     address.primary = True
    #     address.save()
    #     serializer = self.get_serializer(instance=address)
    #     return response.Response(serializer.data, status=status.HTTP_200_OK)

    # @action(
    #     methods=["PUT", "PATCH"],
    #     detail=False,
    #     permission_classes=[IsPartner],
    #     serializer_class=AddressSerializer,
    #     url_path="me/address/(?P<id>[^/.]+)",
    # )
    # def update_my_address(self, request, id, *args, **kwargs):
    #     """Update selected customer address"""
    #     partner = self.request.user.partner
    #     address = get_object_or_404(PartnerAddress, id=id, partner=partner)
    #     kwargs = {"instance": address, "data": request.data}
    #     if request.method == "PATCH":
    #         kwargs["is_partial"] = True
    #     serializer = self.get_serializer(**kwargs)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(partner=partner)
    #     return response.Response(serializer.data, status=status.HTTP_200_OK)

    # @action(
    #     methods=["DELETE"],
    #     detail=False,
    #     permission_classes=[IsPartner],
    #     url_path="me/address/(?P<id>[^/.]+)",
    # )
    # def remove_my_address(self, request, id, *args, **kwargs):
    #     """Update selected customer address"""
    #     partner = self.request.user.partner
    #     address = get_object_or_404(PartnerAddress, id=id, partner=partner)
    #     if partner.address.objects.count() <= 1 or address.primary:
    #         raise PermissionDenied(_("Deleting primary address is not allowed"))
    #     address.delete()
    #     return response.Response({"message": _("Your address deleted")}, status=status.HTTP_200_OK)
