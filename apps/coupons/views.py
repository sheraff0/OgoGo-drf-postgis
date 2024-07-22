from random import choice

from django.utils.timezone import now
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from contrib.utils.serializers import validate_and_serialize

from apps.offers.querysets import calendar_filter
from apps.offers.serializers import OfferSearchResultsSerializer
from .models import Coupon
from .serializers import CouponSerializer, CouponRequireSerializer


class CouponViewSet(ListModelMixin, GenericViewSet):
    http_method_names = ["get", "post"]

    def get_queryset(self):
        return Coupon.objects.related().filter(
            user=self.request.user
        ).order_by("-create_time")

    def get_serializer_class(self):
        if self.action == "list":
            return CouponSerializer
        elif self.action == "issue":
            return CouponRequireSerializer

    @action(detail=False, methods=["post"])
    def issue(self, request, *args, **kwargs):
        request_data = validate_and_serialize(self.get_serializer_class(), self.request.data)
        quantity = request_data.pop("quantity", 1)
        if res := calendar_filter(**request_data):
            closest = res[0]["wait"]
            offer = choice([x for x in res if x["wait"] == closest])
            fixed_time = offer["offer"]["fixed_time"]
            start = max(now(), offer["open_time"])
            duration=offer["close_time"] - start
            coupon_obj = Coupon.objects.create(
                user=request.user,
                offer_id=offer["offer"]["id"],
                start=start,
                duration=duration,
                quantity=quantity,
                price=quantity * (offer["offer"]["price"] or 0),
            )
            coupon = CouponSerializer(coupon_obj).data
            return Response(coupon, status=status.HTTP_200_OK)
        else:
            return Response({"errors": {"details": ["Not found"]}}, status=status.HTTP_404_NOT_FOUND)
