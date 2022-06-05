import requests


TOKEN = "cbce9130cbce9130cbce913040cbb276eaccbcecbce9130a95253a5b1f70dc4fa426c01"
VERSION = 5.131

USER_ID = int(input("Введите id пользователя ВКонтакте: "))

r = []
try:
    r = requests.get("https://api.vk.com/method/friends.get", params={
        "user_id": USER_ID,
        "order": "name",
        "fields": "domain",
        "access_token": TOKEN,
        "v": VERSION
    }).json()["response"]["items"]
except KeyError:
    print("This profile is private")
all_friends = []
for i in range(len(r)):
    friend = r[i].get("first_name") + " " + r[i].get("last_name") + ": vk.com/" + r[i].get("domain")
    all_friends.append(friend)
for i in range(len(all_friends)):
    print(all_friends[i])
print(f"Total:{len(all_friends)}")
