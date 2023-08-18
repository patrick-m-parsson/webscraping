import requests

# Replace with your access token
access_token = "EAABwzLixnjYBO1472BLgIq7eJeEV0zdvAZBHGybwe38FaFsnZCZBpXyKo89NwuHzZCAHFn0tngV7FIbaDJBD0tfOloZCPlnIxMY5wjb6fgS1VvVLRZBoUryzg3tRXRzmf2Gs1bR6ZAIpG2nRv0xWZBAdZAlPdTqTwQf4v6XZAtoNoPik4Ox2RqgZAWJiOBENxcY9mdpT31jN6JtAGVkNjvG6N1l"

# Replace with the group ID you want to post to
# group_id = "1000577781067199"
group_id = "2165467720309534"

# The URL for posting in the group
post_url = f"https://graph.facebook.com/{group_id}/feed"

# Data for the post
post_data = {
    "message": "Hello, this is a test post from Python!"
}

# Add access token to the data
post_data["access_token"] = access_token

# Make the POST request to post in the group
response = requests.post(post_url, data=post_data)

# Check the response
if response.status_code == 200:
    print("Post successful!")
else:
    print("Post failed.")
    print(response.json())
