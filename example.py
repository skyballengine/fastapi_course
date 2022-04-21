# without response_model PostResponse with return results with join
{
    "Post": {
        "content": "rahhhh",
        "title": "sweet time",
        "created_at": "2022-04-11T22:05:33.290815-04:00",
        "id": 22,
        "published": true,
        "owner_id": 21,
    },
    "votes": 0,
}

# with response_model PostResponse with return posts
# what pydantic expects because follows the response_model
{
    "title": "first post",
    "content": "gibberish",
    "published": true,
    "id": 3,
    "created_at": "2022-04-11T14:35:41.714791-04:00",
    "owner_id": 21,
    "owner": {
        "id": 21,
        "email": "jon@yahoo.com",
        "created_at": "2022-04-10T21:16:08.397517-04:00",
    },
}
