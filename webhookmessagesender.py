import requests

webhook_url = input("what is the webhook link ")

message = {
    "content":input("what message you want to send "),
    "username":input("what would be the bot's username ")
}

send = requests.post(webhook_url,json=message)
response_error = requests.status_codes 
if response_error == 200:
    print("message sent")
