import requests

# Replace with your access token
access_token = "EAABwzLixnjYBO1472BLgIq7eJeEV0zdvAZBHGybwe38FaFsnZCZBpXyKo89NwuHzZCAHFn0tngV7FIbaDJBD0tfOloZCPlnIxMY5wjb6fgS1VvVLRZBoUryzg3tRXRzmf2Gs1bR6ZAIpG2nRv0xWZBAdZAlPdTqTwQf4v6XZAtoNoPik4Ox2RqgZAWJiOBENxcY9mdpT31jN6JtAGVkNjvG6N1l"

# Replace with the group ID you want to retrieve posts from
# group_id = "1000577781067199"
group_id = "2165467720309534"

# The URL for retrieving group posts
posts_url = f"https://graph.facebook.com/{group_id}/feed"

# Parameters for the request
params = {
    "access_token": access_token
}

# Make the GET request to retrieve group posts
response = requests.get(posts_url, params=params)

# Check the response
if response.status_code == 200:
    posts_data = response.json()
    if "data" in posts_data:
        for post in posts_data["data"]:
            print("Post ID:", post.get("id"))
            print("Message:", post.get("message"))
            print("Created Time:", post.get("created_time"))
            print("-" * 30)
else:
    print("Failed to retrieve posts.")
    print(response.json())
