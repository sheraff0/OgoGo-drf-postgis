from django.db import models

from contrib.common.models import UUIDModel


class CouponQuerySet(models.QuerySet):
    def related(self):
        return self.select_related(
            "offer__location"
        ).prefetch_related(
            "offer__options", "offer__categories"
        )


class CouponStatus(str, models.Choices):
    ISSUED = "ISSUED", "Выпущен"
    PAID = "PAID", "Оплачен"
    RESERVED = "RESERVED", "Зарезервирован"
    DONE = "DONE", "Выполнен"
    CANCELLED = "CANCELLED", "Отменен"


CS = CouponStatus

STATUS_TRANSITIONS = {
    CS.ISSUED: [CS.PAID, CS.CANCELLED],
    CS.PAID: [CS.RESERVED, CS.CANCELLED, CS.DONE],
    CS.RESERVED: [CS.CANCELLED, CS.DONE],
    CS.DONE: [],
    CS.CANCELLED: [],
}


class Coupon(UUIDModel):
    user = models.ForeignKey("users.User", verbose_name="Пользователь",
        related_name="coupons", on_delete=models.CASCADE)
    offer = models.ForeignKey("offers.Offer", verbose_name="Предложение",
        related_name="coupons", on_delete=models.CASCADE)
    start = models.DateTimeField("Дата и время начала", null=True, blank=True)
    duration = models.DurationField("Продолжительность", null=True, blank=True)
    quantity = models.IntegerField("Количество", default=0)
    price = models.IntegerField("Цена", default=0)
    status = models.CharField("Статус", max_length=16, choices=CouponStatus.choices, default=CouponStatus.ISSUED)

    objects = CouponQuerySet.as_manager()

    def __str__(self):
        return "{} - {}".format(
            self.user.email,
            self.offer.location.__str__()
        )

    class Meta:
        verbose_name = "Купон"
        verbose_name_plural = "Купоны"
