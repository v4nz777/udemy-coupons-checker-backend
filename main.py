from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import scraper


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scrape/{course}/{coupon}/{fast}")
async def root(course:str, coupon:str, fast:bool) -> object:
    url = f"https://www.udemy.com/course/{course}/?couponCode={coupon}"
    course_details, coupon_details = scraper.scrape(course,coupon,fast)
    course_name = course_details['title']
    is_free = coupon_details["purchase"]["data"]["pricing_result"]["price"]["amount"] == 0
        

    return {
        "course":course_name,
        "coupon": coupon,
        "url":url,
        "details":course_details,
        "coupon_details": coupon_details,
        "free": is_free,
        "skipped":False
        }