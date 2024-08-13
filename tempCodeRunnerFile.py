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