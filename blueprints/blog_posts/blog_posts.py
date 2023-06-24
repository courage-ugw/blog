from flask import Blueprint, render_template, request, redirect, url_for
from blog.data_storage.blog_data import BlogData

# Initialize the Blueprint Object
blog_post_bp = Blueprint('blog_posts', __name__, static_folder='static',
                         static_url_path='blog_posts.static',
                         template_folder='templates')

# Initialize the Blog Data Object
blog_data = BlogData()


@blog_post_bp.route('/add', methods=['GET', 'POST'])
def add():
    """ Adds new blog post to the JSON file"""

    # Handles the request, if request method is POST
    if request.method == 'POST':
        # Gets the data from input values of the form
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        # Add blog post
        blog_data.add_blog_post(author=author, title=title, content=content)

        # Redirect back to index
        return redirect(url_for('blog_post_index.index'))

    # Otherwise request method is GET, render the add post form - add.html
    return render_template('add.html')


@blog_post_bp.route('/delete/<int:post_id>')
def delete(post_id):
    """ Delete blog post from the JSON file using id"""

    # Delete post
    blog_data.delete_blog_post(post_id)

    # Redirect back to index
    return redirect(url_for('blog_post_index.index'))


@blog_post_bp.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """ Updates existing blog post in the JSON file"""

    # Fetch the blog posts from the JSON file
    post = blog_data.fetch_post_by_id(post_id)
    if post is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
        # Update the post in the JSON file
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        blog_data.update_blog_post(post_id=post_id, author=author, title=title, content=content)

        # Redirect back to index
        return redirect(url_for('blog_post_index.index'))

    # Else, it's a GET request
    # So display the update.html page
    return render_template('update.html', post=post)


@blog_post_bp.route('/post_likes/<int:post_id>')
def post_likes(post_id):
    """  Handles the like button click. Increment like count  """

    # Fetch the blog posts from the JSON file
    post = blog_data.fetch_post_by_id(post_id)

    # Gets the like count and increment by 1
    new_like_count = post.get('like') + 1

    # update the like count
    blog_data.update_like_count(post_id, new_like_count)

    # Redirect back to index
    return redirect(url_for('blog_post_index.index'))

