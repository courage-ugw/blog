from flask import Blueprint, render_template
from blog.data_storage.blog_data import BlogData

# Initialize the Blueprint Object
blog_post_index_bp = Blueprint('blog_post_index', __name__, static_folder='static',
                               static_url_path='/blog_post_index/static',
                               template_folder='templates')

# Initialize the Blog Data Object
blog_data = BlogData()


@blog_post_index_bp.route('/')
def index():
    """ Displays the home page of the blog """

    blog_posts = blog_data.load_data()  # loads all blog posts
    return render_template('index.html', posts=blog_posts)  # renders the index page

