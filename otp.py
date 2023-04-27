import requests

url = "https://www.fast2sms.com/dev/bulkV2"

def sendsms(num,phone):
    payload = f"sender_id=FTWSMS&message=To Verify Your Mobile NUmber with ZitaApps is {num} &route=v3&numbers={phone}"
    print(payload)
    headers = {
        'authorization': "ulBGWHeNb4qJ9KmyA1fip0RdPYh6kXjwEscTSQ3ODFvC2rgnIZezvgnxpTBcjmlJZQAkY7LKVSHGMU4d",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }
    response="sent"

    response = requests.request("POST", url, data=payload, headers=headers)
    return True


sendsms(98657,8341342208)