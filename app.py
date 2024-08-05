from flask import Flask, render_template, request, jsonify, url_for,redirect ,session , flash
from models import db , Visitor , BlogData ,CommentData , AdminData
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
        data = request.get_json()  # Get JSON data from the client / request body
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
def blog_post_routes():
# Route to view a blog post
    @app.route('/blog', methods=['GET'])
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
        
    #left to do  delete 
    @app.route('/blog/<int:id>', methods=['GET'])     
    def get_blog(id):
        post = BlogData.query.get_or_404(id)
        return render_template('update_blog.html', post=post)

    # GET /blog/<int:id> renders the update form with the current blog data.
    # PUT /blog/<int:id> updates the blog post and returns a JSON response.

    @app.route('/blog/<int:id>', methods=['PUT'])          #updates data
    def update_blog(id):
        post = BlogData.query.get_or_404(id)
        # if request.method == 'POST':
        data = request.get_json()
        post.title = data.get('title', post.title)
        post.content = data.get('content', post.content)
        post.author = data.get('author', post.author)
        db.session.commit()
        return jsonify({'message': 'Blog updated', 'title': post.title})
        # return render_template('update_blog.html', post=post)


    @app.route('/blog/<int:id>', methods=['DELETE'])    #deleting blog
    def delete_blog(id):
        post = BlogData.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()
        return jsonify({'message': 'Blog post deleted'})

# comments functionaltiy

# @app.route('/blog', methods=['POST', 'GET'])
# def add_comment(id):
#     post = BlogData.query.get_or_404(id)
#     data = request.get_json()
#     new_comment = CommentData(
#         content=data['content'],
#         author=data['author'],
#         blog=post
#     )
#     db.session.add(new_comment)
#     db.session.commit()
#     return jsonify({'message': 'Comment added'})
    

# @app.route('/blog/<int:post_id>', methods=['GET'])
# def view_blog(id):
#     post = BlogData.query.get_or_404(id)
#     comments = CommentData.query.filter_by(blog_id=id).all()
#     return render_template('view_blog.html', post=post, comments=comments)

def admin_routes():
    @app.route('/admin/login', methods=['GET', 'POST'])
    def admin_login():
        if request.method == "POST":
            username= request.form['username']
            password= request.form['password']
            admin = AdminData.query.filter_by(username= username).first()
            if admin and admin.check_password(password):        #if admin record was found and password matches
                session['admin'] = admin.username               #If the login is successful, the admin's username is stored in the session
                return redirect(url_for('admin_dashboard'))
            flash('Invalid username or password')               #if login fails
        return render_template('admin_login.html')

    @app.route('/admin/dashboard')
    def admin_dashboard():
        if 'admin' not in session:
            return redirect(url_for('admin_login'))
        return render_template('admin_dashboard.html')

    @app.route('/admin/logout')
    def admin_logout():
        session.clear()
        return redirect(url_for('admin_login'))

if __name__ == '__main__':
    admin_routes()
    blog_post_routes()
    app.run(debug=True)