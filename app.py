from flask import Flask
from blueprints.blog_post_index.blog_post_index import blog_post_index_bp
from blueprints.blog_posts.blog_posts import blog_post_bp

# Initialize Flask
app = Flask(__name__)

# Register Blueprints
app.register_blueprint(blog_post_index_bp)
app.register_blueprint(blog_post_bp, url_prefix='/blog_post')


if __name__ == '__main__':
    app.run(debug=True)