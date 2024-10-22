from random import randint

from src.utilities.requestsUtility import RequestsUtility
import random
import string

class CouponHelper(object):
    def __init__(self):
        self.request_utility = RequestsUtility()

    def create_percentage_coupon(self, code=None, discount_type="percent", amount=None, expected_status_code = 201, **kwargs):

        if not code:
            code = "".join(random.choices(string.ascii_lowercase, k=10))
        if not amount:
            amount = str(randint(1, 100))


        payload = dict()
        payload["code"] = code
        payload["discount_type"] = discount_type
        payload["amount"] = amount
        payload.update(kwargs)

        create_coupon_json = self.request_utility.post("coupons", payload = payload, expected_status_code= expected_status_code)

        return create_coupon_json


