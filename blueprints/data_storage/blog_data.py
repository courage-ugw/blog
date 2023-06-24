import json
from uuid import uuid4

# JSON file path
FILE_PATH = 'blog_posts'

# Initial data to populate JSON file if file does not exist
INITIAL_BLOG_POSTS = [
    {'id': 1,
     'author': 'John Doe',
     'title': 'First Post',
     'content': 'This is my first post.',
     'like': 0},

    {'id': 2,
     'author': 'Jane Doe',
     'title': 'Second Post',
     'content': 'This is another post.',
     'like': 0},
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

    # Creates file if it does not exist. If file exists do nothig
    create_file()

    # Load data from JSON file
    with open(FILE_PATH, 'r') as json_file:
        blog_data = json.load(json_file)
    return blog_data


def save_data(data):
    """ Save Blog Data to JSON File """

    with open(FILE_PATH, 'w') as json_file:
        json.dump(data, json_file)


def add_blog_post(author, title, content):
    """ Adds new blog post to JSON file """

    # Load all blog posts from JSON file
    blog_posts = load_data()

    # Generate unique id (int) for post using the uuid4()
    # Insert the newly added blog post at the top
    blog_posts.insert(0, {
        'id': uuid4().int,
        'author': author,
        'title': title,
        'content': content,
        'like': 0})

    # Save blog post to JSON file
    save_data(blog_posts)
    return 'post added!'


def update_blog_post(post_id, author, title, content):
    """ Updates an existing blog post """

    # Load all blog posts from JSON file
    blog_posts = load_data()

    # Update blog post
    blog_post_index = 0
    for blog_post in blog_posts:
        if blog_post['id'] == post_id:
            blog_post['author'] = author
            blog_post['title'] = title
            blog_post['content'] = content

            # Gets blog post index
            blog_post_index = blog_posts.index(blog_post)

    # remove the updated blog post from the list using the blog post index
    updated_blog_post = blog_posts.pop(blog_post_index)

    # Insert the updated blog post at the top or (zero index of the list)
    blog_posts.insert(0, updated_blog_post)

    # Save blog post to JSON file
    save_data(blog_posts)
    return 'post updated!'


def delete_blog_post(post_id):
    """ Delete blog post from JSON file """

    # Load all blog posts from JSON file
    blog_posts = load_data()

    # Delete blog post with a given post_id
    for blog_post in blog_posts:
        if blog_post['id'] == post_id:
            blog_post_index = blog_posts.index(blog_post)
            blog_posts.pop(blog_post_index)

            # Save blog post to JSON file
            save_data(blog_posts)
            return 'Post deleted!'
    return 'Post not found'


def fetch_post_by_id(post_id):
    """ Fetch blog post by post id """

    blog_posts = load_data()
    for blog_post in blog_posts:
        if blog_post['id'] == post_id:
            return blog_post


def update_like_count(post_id, new_like_count):
    """ Updates like count of a blog post """

    # Load all blog posts from JSON file
    blog_posts = load_data()

    # Update like count of a post
    for blog_post in blog_posts:
        if blog_post['id'] == post_id:
            blog_post['like'] = new_like_count

    # Save blog post to JSON file
    save_data(blog_posts)