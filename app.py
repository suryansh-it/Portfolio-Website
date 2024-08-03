from flask import Flask, render_template, request, jsonify, url_for,redirect
from models import db , Visitor , BlogData
from flask_migrate import Migrate




def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0904@localhost:5432/visitors'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)



    with app.app_context():
        db.create_all()  # Create tables based on the model definitions

    return app

app= create_app()

migrate = Migrate(app, db)

@app.route('/')
def index():
    
    return render_template('index.html')
    


# @app.route('/Home')
# def home():
#     return render_template('Home.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Projects')
def Projects():
    return render_template('Projects.html')


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        data = request.get_json()  # Get JSON data from the client
        new_visitor = Visitor(
            name=data['name'],
            email=data['email'],
            subject=data['subject'],
            message=data.get('message', '')
        )
        db.session.add(new_visitor)
        db.session.commit()

        return jsonify({
            'messagecontent': f'Form submitted successfully, name: {data["name"]}, email: {data["email"]}, '
                              f'subject: {data["subject"]}, message: {data["message"]}'
        })
    return render_template('form.html')



# Blog post routes

# Route to view a blog post
@app.route('/view_blog', methods=['GET'])
def blog():

    if request.method == 'POST':
        return redirect(url_for('create_blog'))

    posts = BlogData.query.all()  # Fetch all blog posts
    if not posts:
        # Return a message or redirect if no posts exist
        return render_template('view_blog.html', posts=None)
    return render_template('view_blog.html', posts=posts)


@app.route('/create_blog', methods=['POST', 'GET'])
def create_blog():
    if request.method == 'POST':
        data = request.get_json()  # Get JSON data from the client
        new_blog = BlogData(
            title=data['title'],
            content=data['content'],
            author=data['author'],    
        )
        db.session.add(new_blog)
        db.session.commit()
        # return redirect(url_for('view_blog'))
        return jsonify({
            'messagecontent': 'Blog created successfully','title' :new_blog.title 
        } )
    return render_template('create_blog.html')


# @app.route('/view_blog/<int:id>', methods=["GET"])
# def get_blog(id):
    
#     post = BlogData.query.get_or_404(id)
#     if  request.method == 'POST':
#         return jsonify({                    #returns the data via GET
#             'id': post.id,
#             'title': post.title,
#             'content': post.content,
#             'author': post.author,
#             'date_created': post.date_created
#         } )
#     return render_template('view_blog.html', post=post)
    
#left to do update , delete 

@app.route('/view_blog/<int:id>', methods=['PUT'])           #updates data
def update_blog(id):
    post = BlogData.query.get_or_404(id)
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    post.author = data.get('author', post.author)
    db.session.commit()
    return jsonify({'message': 'Blog updated', 'title': post.title}, post = post)

@app.route('/view_blog/<int:id>', methods=['DELETE'])    #deleting blog
def delete_blog(id):
    post = BlogData.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Blog post deleted'}, post = post)


if __name__ == '__main__':
    app.run(debug=True)