from flask import Flask , request , url_for, redirect , render_template , jsonify

app = Flask(__name__)

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


@app.route('/form' , methods=['POST','GET'])
def form():
    if request.method == 'POST':
        data = request.get_json
        name = data.get('name')
        email = data.get('email')

        return jsonify({'messege': 'Form submitted successfully', 'name': name, 'email': email})

    return render_template('form.html')




if __name__ == '__main__':
    app.run(debug=True)