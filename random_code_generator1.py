import random
import string

coupon_number = 20
coupon_size = 15

for i in range(coupon_number):
    coupon = ''.join(
        random.sample(string.digits + string.ascii_uppercase, coupon_size))
    print(coupon)
