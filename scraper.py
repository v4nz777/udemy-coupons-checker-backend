import requests
import json
import time
import random
from headers import USER_AGENTS, ACCEPT_LANGUAGES


def scrape(course_id:str,coupon:str,fast:bool) -> tuple:
    # Set 3 sec interval
    if not fast:
        time.sleep(random.uniform(0.5,2))

    # Get course details.
    print('Getting details...')
    res1 = requests.get(f'https://www.udemy.com/api-2.0/courses/{course_id}', headers={
        'User-Agent': random.choice(USER_AGENTS),
        'Accept-Language': random.choice(ACCEPT_LANGUAGES)
    })
    course_details = json.loads(res1.content)
    _course_id = course_details['id']
    # Set 3 sec interval
    if not fast:
        time.sleep(random.uniform(0.5,2))

    # Get coupon details
    print('Getting coupon...')
    res2 = requests.get(f'https://www.udemy.com/api-2.0/course-landing-components/{_course_id}/me/?couponCode={coupon}&components=slider_menu,buy_button,deal_badge,discount_expiration,price_text,incentives,purchase,redeem_coupon,money_back_guarantee,base_purchase_section,purchase_tabs_context,lifetime_access_context,available_coupons,gift_this_course,buy_for_team', headers={
        'User-Agent': random.choice(USER_AGENTS),
        'Accept-Language': random.choice(ACCEPT_LANGUAGES)
    })
    coupon_details = json.loads(res2.content)

    return (course_details, coupon_details)
