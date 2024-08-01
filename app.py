from flask import Flask, render_template, request, jsonify, url_for
from .models import db

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
        new_visitor = Prof_data(
            name = data['name'], 
            email = data['email'], 
            subject = data['subject'], 
            message = data.get('message',{}))
        
    db.session.add(new_visitor)
    db.session.commit()
    return jsonify({'message': 'visitor created', 'name': new_visitor.name}), 201
     #!!reminder: formatted string for each line
    #return json data to client
        


    return render_template('form.html')




if __name__ == '__main__':
    app.run(debug=True)