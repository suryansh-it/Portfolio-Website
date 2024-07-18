from flask import Flask, render_template, request, jsonify, url_for

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
        data = request.get_json() #get json data from client
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        
        return jsonify({'messagecontent': f'Form submitted successfully, name: {name}, email: {email},'
                        f' subject:{subject}, message: {message}' })     #!!reminder: formatted string for each line
    #return json data to client
        


    return render_template('form.html')




if __name__ == '__main__':
    app.run(debug=True)