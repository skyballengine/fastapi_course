my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "Favorite foods", "content": "I like enchiladas", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def get_post_index(id):
    for index, post in enumerate(my_posts):
        if post["id"] == id:
            return index