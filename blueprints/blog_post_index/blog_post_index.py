from flask import Blueprint, render_template
from blog.blueprints.data_storage.blog_data import load_data

# Initialize the Blueprint Object
blog_post_index_bp = Blueprint('blog_post_index', __name__, static_folder='static',
                         static_url_path='/blog_post_index/static', template_folder='templates')


@blog_post_index_bp.route('/')
def index():
    blog_posts = load_data()
    return render_template('index.html', posts=blog_posts)