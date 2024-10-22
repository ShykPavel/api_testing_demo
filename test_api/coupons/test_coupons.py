from src.helpers.coupons_helper import CouponHelper
from src.dao.coupons_dao import CouponsDAO

coupon_helper = CouponHelper()
coupon_dao = CouponsDAO()


def test_create_percentage_coupon():

    coupon_api = coupon_helper.create_percentage_coupon()
    coupon_id = coupon_api['id']
    coupon_api_amount = str(coupon_api["amount"]).replace(".00","")

    coupon_amount_db = coupon_dao.get_coupon_metadata_from_db_by_key(coupon_id, "coupon_amount")
    coupon_discount_type_db = coupon_dao.get_coupon_metadata_from_db_by_key(coupon_id, "discount_type")

    assert coupon_api["discount_type"] == coupon_discount_type_db["meta_value"], "Coupon discount type is different in API and Database"
    assert coupon_api_amount == coupon_amount_db["meta_value"], "Coupon amount is different in API and Database"




