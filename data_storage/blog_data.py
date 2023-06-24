import json
from uuid import uuid4


class BlogData:
    """ Executes all the CRUD actions on blog site """

    def __init__(self):
        """ Constructor for Blog Data Class. """

        # JSON file path
        self.file_path = 'blog_posts'

        # Initial data to populate JSON file if file does not exist
        self.initial_blog_posts = [
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

    def create_file(self):
        """ Create and initialize JSON File. If file exists do nothing """

        try:
            with open(self.file_path, 'x') as json_file:
                json.dump(self.initial_blog_posts, json_file)
        except FileExistsError:
            pass

    def load_data(self) -> list:
        """ Load Data from JSON """

        # Creates file if it does not exist. If file exists do nothig
        self.create_file()

        # Load data from JSON file
        with open(self.file_path, 'r') as json_file:
            blog_data = json.load(json_file)
        return blog_data

    def save_data(self, data):
        """ Save Blog Data to JSON File """

        with open(self.file_path, 'w') as json_file:
            json.dump(data, json_file)

    def add_blog_post(self, author, title, content):
        """ Adds new blog post to JSON file """

        # Load all blog posts from JSON file
        blog_posts = self.load_data()

        # Generate unique id (int) for post using the uuid4()
        # Insert the newly added blog post at the top
        blog_posts.insert(0, {
            'id': uuid4().int,
            'author': author,
            'title': title,
            'content': content,
            'like': 0})

        # Save blog post to JSON file
        self.save_data(blog_posts)
        return 'post added!'

    def update_blog_post(self, post_id, author, title, content):
        """ Updates an existing blog post """

        # Load all blog posts from JSON file
        blog_posts = self.load_data()

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
        self.save_data(blog_posts)
        return 'post updated!'

    def delete_blog_post(self, post_id):
        """ Delete blog post from JSON file """

        # Load all blog posts from JSON file
        blog_posts = self.load_data()

        # Delete blog post with a given post_id
        for blog_post in blog_posts:
            if blog_post['id'] == post_id:
                blog_post_index = blog_posts.index(blog_post)
                blog_posts.pop(blog_post_index)

                # Save blog post to JSON file
                self.save_data(blog_posts)
                return 'Post deleted!'
        return 'Post not found'

    def fetch_post_by_id(self, post_id):
        """ Fetch blog post by post id """

        blog_posts = self.load_data()
        for blog_post in blog_posts:
            if blog_post['id'] == post_id:
                return blog_post

    def update_like_count(self, post_id, new_like_count):
        """ Updates like count of a blog post """

        # Load all blog posts from JSON file
        blog_posts = self.load_data()

        # Update like count of a post
        for blog_post in blog_posts:
            if blog_post['id'] == post_id:
                blog_post['like'] = new_like_count

        # Save blog post to JSON file
        self.save_data(blog_posts)