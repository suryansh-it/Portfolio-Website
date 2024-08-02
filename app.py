from flask import Flask, render_template, request, jsonify, url_for
from models import db , Visitor



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

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Home')
def home():
    return render_template('Home.html')

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


if __name__ == '__main__':
    app.run(debug=True)