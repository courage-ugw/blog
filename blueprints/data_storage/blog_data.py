import json
from uuid import uuid4

FILE_PATH = 'blog_posts'

INITIAL_BLOG_POSTS = [
    {'id': 1,
     'author': 'John Doe',
     'title': 'First Post',
     'content': 'This is my first post.'},
    {'id': 2,
     'author': 'Jane Doe',
     'title': 'Second Post',
     'content': 'This is another post.'},
    # More blog posts can go here...
]


def create_file():
    """ Create and initialize JSON File. If file exists do nothing """

    try:
        with open(FILE_PATH, 'x') as json_file:
            json.dump(INITIAL_BLOG_POSTS, json_file)
    except FileExistsError:
        pass


def load_data() -> list:
    """ Load Data from JSON """
    create_file()  # creates file if it does not exist. If file exists do nothig
    with open(FILE_PATH, 'r') as json_file:
        blog_data = json.load(json_file)
    return blog_data


def save_data(data):
    """ Save Blog Data to JSON """

    with open(FILE_PATH, 'w') as json_file:
        json.dump(data, json_file)


def add_blog_post(author, title, content):
    blog_posts = load_data()
    blog_posts.append({
        'id': uuid4().int,
        'author': author,
        'title': title,
        'content': content})
    save_data(blog_posts)
    return 'post added!'


def delete_blog_post(post_id):
    blog_posts = load_data()
    for blog_post in blog_posts:
        if blog_post['id'] == post_id:
            blog_post_index = blog_posts.index(blog_post)
            blog_posts.pop(blog_post_index)
            save_data(blog_posts)
            return 'Post deleted!'
    return 'Post not found'


def fetch_post(post_id):
    blog_posts = load_data()

    post = []
    for blog_post in blog_posts:
        if blog_post['id'] == post_id:
            post.extend((blog_post['author'], blog_post['title'], blog_post['content']))
            break

    return post
