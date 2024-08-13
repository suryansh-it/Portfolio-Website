# from flask import Flask, render_template, request, jsonify, url_for,redirect ,session , flash
# from models import db , Visitor , BlogData ,CommentData ,ProjectData, AdminData, AboutSection
# from flask_migrate import Migrate
 




# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'your_secret_key'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0904@localhost:5432/visitors'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     db.init_app(app)



#     with app.app_context():
#         db.create_all()  # Create tables based on the model definitions

        
#     return app

# app= create_app()
# migrate = Migrate(app, db)



# def create_admin_user(username, password):
#     # Create a new AdminData instance with the provided username
#     admin = AdminData(username=username)
#     # Hash the provided password and store it in the admin instance
#     admin.set_password(password)
#     db.session.add(admin)
#     db.session.commit()




# @app.route('/')
# def index():
    
#     return render_template('index.html')




# # ----------About Routes----------
# def about_routes():
#     @app.route('/about', methods=['GET', 'POST'])
#     def about():
#         about_section = AboutSection.query.first()
#         if request.method == 'POST':
#             data = request.get_json()
#             new_about = AboutSection(content=data['content'])
#             db.session.add(new_about)
#             db.session.commit()
#             return jsonify({'message': 'About section updated successfully'})
        
#         return render_template('about.html', about=about_section)




# # ----------Project Routes----------
# def project_routes():
#     @app.route('/Project', methods=[ 'GET'])
#     def Projects():
#         projects = ProjectData.query.all()
#         return render_template('view_project.html', projects=projects)


  

# # ----------Contact Form Routes----------
# def contact_form_route():
#     @app.route('/form', methods=['POST', 'GET'])
#     def form():
#         if request.method == 'POST':
#             data = request.get_json()  # Get JSON data from the client / request body
#             new_visitor = Visitor(
#                 name=data['name'],
#                 email=data['email'],
#                 subject=data['subject'],
#                 message=data.get('message', '')
#             )
#             db.session.add(new_visitor)
#             db.session.commit()

#             return jsonify({
#                 'messagecontent': f'Form submitted successfully, name: {data["name"]}, email: {data["email"]}, '
#                                 f'subject: {data["subject"]}, message: {data["message"]}'
#             })
#         return render_template('form.html')




# # ----------Blog Post Routes----------
# def blog_post_routes():
# # Route to view a blog post
#     @app.route('/blog', methods=['GET'])
#     def blog():

#         if request.method == 'POST':
#             return redirect(url_for('create_blog'))

#         posts = BlogData.query.all()  # Fetch all blog posts
#         if not posts:
#             # Return a message or redirect if no posts exist
#             return render_template('view_blog.html', posts=None)
#         return render_template('view_blog.html', posts=posts)


    


#     # @app.route('/view_blog/<int:id>', methods=["GET"])
#     # def get_blog(id):
        
#     #     post = BlogData.query.get_or_404(id)
#     #     if  request.method == 'POST':
#     #         return jsonify({                    #returns the data via GET
#     #             'id': post.id,
#     #             'title': post.title,
#     #             'content': post.content,
#     #             'author': post.author,
#     #             'date_created': post.date_created
#     #         } )
#     #     return render_template('view_blog.html', post=post)
        
    
   

#     # GET /blog/<int:id> renders the update form with the current blog data.
#     # PUT /blog/<int:id> updates the blog post and returns a JSON response.

    


# # ----------Admin Routes----------
# def admin_routes():

#     @app.route('/admin/login', methods=['GET', 'POST'])
#     def admin_login():
#         if request.method == "POST":
#             username= request.form['username']
#             password= request.form['password']
#             admin = AdminData.query.filter_by(username= username).first()
#             if admin and admin.check_password(password):        #if admin record was found and password matches
#                 session['admin'] = admin.username               #If the login is successful, the admin's username is stored in the session
#                 return redirect(url_for('admin'))
#             flash('Invalid username or password')               #if login fails
#         return render_template('admin_login.html')

#     @app.route('/admin',methods=['GET', 'POST'])
#     def admin():
#         if 'admin' not in session:
#             return redirect(url_for('admin_login'))
#         return render_template('admin.html')
    
#     @app.route('/admin/dashboard',methods=['GET', 'POST'])
#     def admin_dashboard():
#         # project = ProjectData.query.all()
#         # post = BlogData.query.all()
#         # about_section = ProjectData.query.all()
#         admin_dashboard_content()
#         return render_template('admin_dashboard.html')

#     @app.route('/admin/logout',methods=['GET', 'POST'])
#     def admin_logout():
#         session.clear()
#         return redirect(url_for('admin_login'))


# # ----------Admin Dashboard----------
# def admin_dashboard_content():

#     # -----------------ABOUT---------------------

#     @app.route('/admin/dashboard/add_about', methods=['POST', 'GET'])
#     def add_about():
#         if request.method == 'POST':
#             data = request.get_json()  # Get JSON data from the client
#             adding_about = AboutSection(
#                 content=data['content'],
#             )
#             db.session.add(adding_about)
#             db.session.commit()
            
#             return jsonify({
#                 'messagecontent': 'about added successfully'
#             } )                 
#         return render_template('admin_dashboard.html')

#     @app.route('/admin/dashboard/get_about', methods=['GET'])     
#     def get_about():
#         about_section = AboutSection.query.all()
#         return render_template('admin_dashboard.html',about_section=about_section  )

#     @app.route('/admin/dashboard/edit_about',methods=["PUT"])
#     def edit_about():
#         about_section = AboutSection.query.all()
#         data = request.get_json()
#         about_section.content = data.get("content", about_section.content)
#         db.session.commit()
#         return jsonify({'message': 'about updated'})




#     # -----------------PROJECTS---------------------

#     @app.route('/admin/dashboard/add_project', methods=['POST', 'GET'])
#     def add_project():
#         if request.method == 'POST':
#             data = request.get_json()  # Get JSON data from the client
#             new_project = ProjectData(
#                 project_name=data['project_name'],
#                 project_summary=data['project_summary'],
                  
#             )
#             db.session.add(new_project)
#             db.session.commit()
            
#             return jsonify({
#                 'messagecontent': 'project added successfully','title' :new_project.project_name 
#             } )                 
#         return render_template('add_project.html')

    
#     @app.route('/admin/dashboard/get_project/<int:project_id>', methods=['GET'])     
#     def get_project(project_id):
#         project = ProjectData.query.get_or_404(project_id)
#         return render_template('admin_dashboard.html', project= project)
    

#     @app.route('/admin/dashboard/select_project/<int:project_id>', methods=['POST'])
#     def select_project(project_id):
#         total_projects = ProjectData.query.count()
#         project_number = request.form.get('project_number')
#         if project_number :
#             if project_number <= total_projects:
#                 project_number = project_id
#             else:
#                     flash("Project not found", "danger")
#         return redirect(url_for('admin_dashboard'))            


#     @app.route('/admin/dashboard/edit_projects/<int:project_id>',methods=["PUT"])
#     def edit_projects(project_id):
#         project = ProjectData.query.get_or_404(project_id)
#         data = request.get_json()
#         project.project_name = data.get('project_name',project.project_name)
#         project.project_summary = data.get('project_summary',project.project_summary)
#         db.session.commit()
#         return jsonify({'message': 'project updated', 'project_name': project.project_name})


#     @app.route('/admin/dashboard/delete_project/<int:project_id>', methods=['DELETE'])    #deleting project
#     def delete_project(project_id):
#         project = ProjectData.query.get_or_404(project_id)
#         db.session.delete(project)
#         db.session.commit()
#         return jsonify({'message': 'project post deleted'})





#     # -----------------BLOGS---------------------

#     @app.route('/admin/dashboard/create_blog', methods=['POST', 'GET'])
#     def create_blog():
#         if request.method == 'POST':
#             data = request.get_json()  # Get JSON data from the client
#             new_blog = BlogData(
#                 title=data['title'],
#                 content=data['content'],
#                 author=data['author'],    
#             )
#             db.session.add(new_blog)
#             db.session.commit()
#             # return redirect(url_for('view_blog'))
#             return jsonify({
#                 'messagecontent': 'Blog created successfully','title' :new_blog.title 
#             } )
#         return render_template('create_blog.html')





#     @app.route('/admin/dashboard/get_blog/<int:blog_id>', methods=['GET'])     
#     def get_blog(blog_id):
#         post = BlogData.query.get_or_404(blog_id)
#         return render_template('update_blog.html', post=post)


#     @app.route('/admin/dashboard/select_blog/<int:blog_id>', methods=['POST'])
#     def select_blog(blog_id):
#         total_blogs = BlogData.query.count()
#         blog_number = request.form.get('blog_number')
#         if blog_number :
#             if blog_number <= total_blogs:
#                 blog_number = blog_id
#             else:
#                     flash("blog not found", "danger")
#         return redirect(url_for('admin_dashboard'))  


#     @app.route('/admin/dashboard/update_blog/<int:blog_id>', methods=['PUT'])          #updates data
#     def update_blog(blog_id):
#         post = BlogData.query.get_or_404(blog_id)
#         # if request.method == 'POST':
#         data = request.get_json()
#         post.title = data.get('title', post.title)
#         post.content = data.get('content', post.content)
#         post.author = data.get('author', post.author)
#         db.session.commit()
#         return jsonify({'message': 'Blog updated', 'title': post.title})
#         # return render_template('update_blog.html', post=post)


#     @app.route('/admin/dashboard/delete_blog/<int:blog_id>', methods=['DELETE'])    #deleting blog
#     def delete_blog(blog_id):
#         post = BlogData.query.get_or_404(blog_id)
#         db.session.delete(post)
#         db.session.commit()
#         return jsonify({'message': 'Blog post deleted'})




# if __name__ == '__main__':
#     about_routes()
#     contact_form_route()
#     project_routes()
#     admin_routes()
#     blog_post_routes()
#     # admin_dashboard_content()
    
#     app.run(debug=True)






# # comments functionaltiy

# # @app.route('/blog', methods=['POST', 'GET'])
# # def add_comment(id):
# #     post = BlogData.query.get_or_404(id)
# #     data = request.get_json()
# #     new_comment = CommentData(
# #         content=data['content'],
# #         author=data['author'],
# #         blog=post
# #     )
# #     db.session.add(new_comment)
# #     db.session.commit()
# #     return jsonify({'message': 'Comment added'})
    

# # @app.route('/blog/<int:post_id>', methods=['GET'])
# # def view_blog(id):
# #     post = BlogData.query.get_or_404(id)
# #     comments = CommentData.query.filter_by(blog_id=id).all()
# #     return render_template('view_blog.html', post=post, comments=comments)



# ====================REFINED CODE BY CHAT GPT================================


from flask import Flask, render_template, request, jsonify, url_for, redirect, session, flash
from models import db, Visitor, BlogData, ProjectData, AdminData, AboutSection
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

app = create_app()
migrate = Migrate(app, db)

def create_admin_user(username, password):
    admin = AdminData(username=username)
    admin.set_password(password)
    db.session.add(admin)
    db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

# About Routes
@app.route('/about', methods=['GET', 'POST'])
def about():
    about_section = AboutSection.query.first()
    if request.method == 'POST':
        data = request.get_json()
        new_about = AboutSection(content=data['content'])
        db.session.add(new_about)
        db.session.commit()
        return jsonify({'message': 'About section updated successfully'})
    
    return render_template('about.html', about=about_section)

# Project Routes
@app.route('/Project', methods=['GET'])
def Projects():
    projects = ProjectData.query.all()
    return render_template('view_project.html', projects=projects)

# Contact Form Routes
@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        data = request.get_json()
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

# Blog Post Routes
@app.route('/blog', methods=['GET'])
def blog():
    if request.method == 'POST':
        return redirect(url_for('create_blog'))

    posts = BlogData.query.all()
    if not posts:
        return render_template('view_blog.html', posts=None)
    return render_template('view_blog.html', posts=posts)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        admin = AdminData.query.filter_by(username=username).first()
        if admin and admin.check_password(password):
            session['admin'] = admin.username
            return redirect(url_for('admin'))
        flash('Invalid username or password')
    return render_template('admin_login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'admin' not in session:
        return redirect(url_for('admin_login'))
    return render_template('admin.html')

@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
    selected_project_id = session.get('selected_project_id')
    selected_project = None
    if 'selected_project_id' :
        selected_project = ProjectData.query.get(selected_project_id)
    

    selected_blog_id = session.get('selected_blog_id')
    selected_blog = None
    if 'selected_blog_id' :
        selected_blog = BlogData.query.get(selected_blog_id)

    visitors = Visitor.query.order_by(Visitor.timestamp.desc()).all()
    

    return render_template('admin_dashboard.html', project = selected_project,visitors=visitors, post = selected_blog)

@app.route('/admin/logout', methods=['GET', 'POST'])
def admin_logout():
    session.clear()
    return redirect(url_for('admin_login'))

# Admin Dashboard Routes
@app.route('/admin/dashboard/add_about', methods=['POST', 'GET'])
def add_about():
    if request.method == 'POST':
        data = request.get_json()
        adding_about = AboutSection(
            content=data['content'],
        )
        db.session.add(adding_about)
        db.session.commit()
        
        return jsonify({
            'messagecontent': 'about added successfully'
        })
    return render_template('admin_dashboard.html')

@app.route('/admin/dashboard/get_about', methods=['GET'])
def get_about():
    about_section = AboutSection.query.all()
    return render_template('admin_dashboard.html', about_section=about_section)

@app.route('/admin/dashboard/edit_about', methods=["PUT"])
def edit_about():
    about_section = AboutSection.query.all()
    data = request.get_json()
    about_section.content = data.get("content", about_section.content)
    db.session.commit()
    return jsonify({'message': 'about updated'})

@app.route('/admin/dashboard/add_project', methods=['POST','GET'])
def add_project():
    if request.method == 'POST':
        data = request.get_json()
        new_project = ProjectData(
            project_name=data['project_name'],
            project_summary=data['project_summary'],
        )
        db.session.add(new_project)
        db.session.commit()
        
        return jsonify({
            'messagecontent': 'project added successfully', 'title': new_project.project_name
        })
    return render_template('create_project.html')

# @app.route('/admin/dashboard/get_project/<int:project_id>', methods=['GET'])
# def get_project(project_id):
#     project = ProjectData.query.get_or_404(project_id)
#     return render_template('admin_dashboard.html', project=project)

@app.route('/admin/dashboard/select_project', methods=['POST'])
def select_project():
    
    project_number = request.form.get('project_number')
    # Convert project_number to int and validate it
    try:
        project_number = int(project_number)
    except ValueError:
        flash("Invalid project number", "danger")
        return redirect(url_for('admin_dashboard'))
    
    total_projects = ProjectData.query.count()
    
    # if 1 <= project_number <= total_projects:
    if project_number:
        selected_project = ProjectData.query.filter_by(project_id=project_number).first()
        if selected_project:
            session['selected_project_id'] = selected_project.project_id
            flash(f"Project {selected_project.project_name} selected", "success")
        else:
            flash("Project not found", "danger")
    else:
        flash("Project number out of range", "danger")
    
    return redirect(url_for('admin_dashboard'))


# @app.route('/admin/dashboard/get_project/<int:project_id>', methods=['GET'])
# def get_project(project_id):
#     project = ProjectData.query.get_or_404(project_id)
#     return render_template('edit_projects.html', project=project)

@app.route('/admin/dashboard/edit_projects/<int:project_id>', methods=["PUT","GET"])
def edit_projects(project_id):
    project = ProjectData.query.get_or_404(project_id)
    if request.method == "PUT":
        
        data = request.get_json()
        project.project_name = data.get('project_name', project.project_name)
        project.project_summary = data.get('project_summary', project.project_summary)
        db.session.commit()
        return jsonify({'message': 'project updated', 'project_name': project.project_name})
    return render_template('edit_projects.html', project=project)

@app.route('/admin/dashboard/delete_project/<int:project_id>', methods=['DELETE','GET'])
def delete_project(project_id):
    project = ProjectData.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'project post deleted'})

@app.route('/admin/dashboard/create_blog', methods=['POST', 'GET'])
def create_blog():
    if request.method == 'POST':
        data = request.get_json()
        new_blog = BlogData(
            title=data['title'],
            content=data['content'],
            author=data['author'],
        )
        db.session.add(new_blog)
        db.session.commit()
        return jsonify({
            'messagecontent': 'Blog created successfully', 'title': new_blog.title
        })
    return render_template('create_blog.html')

@app.route('/admin/dashboard/get_blog/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    post = BlogData.query.get_or_404(blog_id)
    return render_template('update_blog.html', post=post)

@app.route('/admin/dashboard/select_blog', methods=['POST'])
def select_blog():
    blog_number = request.form.get('blog_number')
    
    # Convert blog_number to int and validate it
    try:
        blog_number = int(blog_number)
    except ValueError:
        flash("Invalid blog number", "danger")
        return redirect(url_for('admin_dashboard'))
    
    total_blogs = BlogData.query.count()
    
    # if 1 <= blog_number <= total_blogs:
    if blog_number:
        selected_blog = BlogData.query.filter_by(blog_id=blog_number).first()
        if selected_blog:
            session['selected_blog_id'] = selected_blog.blog_id
            flash(f"blog {selected_blog.title} selected", "success")
        else:
            flash("blog not found", "danger")
    else:
        flash("blog number out of range", "danger")
    
    return redirect(url_for('admin_dashboard')) 


@app.route('/admin/dashboard/update_blog/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    post = BlogData.query.get_or_404(blog_id)
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    post.author = data.get('author', post.author)
    db.session.commit()
    return jsonify({'message': 'Blog updated', 'title': post.title})

@app.route('/admin/dashboard/delete_blog/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    post = BlogData.query.get_or_404(blog_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Blog post deleted'})


# @app.route('/admin/dashboard/view_form', methods=['GET'])
# def view_form():
    


if __name__ == '__main__':
    app.run(debug=True)
