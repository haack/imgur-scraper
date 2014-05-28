import requests
from pymongo import MongoClient

print("Opening mongoDB...")
client = MongoClient('localhost', 27017)

db = client.imagesdb

size = db.images.count()
i = size + 1
print("initial size: ", str(size))

for page in range(0, 50):
	print("Initialising GET request to fetch page...")
	# url = "https://api.imgur.com/3/image/" + str(i)
	url = "https://api.imgur.com/3/gallery/hot/viral/" + str(page)
	r = requests.get(url, headers={"Authorization": "Client-ID 96b446f0b61a180"})

	for image in r.json()['data']:
		print("Adding at index: ", str(i))

		item = {
			"id": i,
			"url": image['link'],
			"rating": 0
		}

		db.images.insert(item)
		i += 1
print("Finishing with size:", str(db.images.count()))
print("Done!")