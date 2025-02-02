from yandex_checkout.domain.common.payment_method_type import PaymentMethodType
from yandex_checkout.domain.models.payment_data.payment_data import ResponsePaymentData


class PaymentDataWechat(ResponsePaymentData):
    def __init__(self, *args, **kwargs):
        super(PaymentDataWechat, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.WECHAT:
            self.type = PaymentMethodType.WECHAT
