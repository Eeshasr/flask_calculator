from flask import Flask,request,render_template,jsonify


app = Flask(__name__)
@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/math', methods = ['POST'])
def math_ops():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add':
           result = num1 + num2
        elif ops == 'subtract':
           result = num1 - num2
        elif ops == 'multiply':
           result = num1 * num2
        elif ops == 'divide':
            result = num1 / num2

    # Render the result template
    return render_template('result.html', result=result)


@app.route('/postman_action', methods=['POST'])
def math_ops1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if ops == 'add':
           result = num1 + num2
        elif ops == 'subtract':
           result = num1 - num2
        elif ops == 'multiply':
           result = num1 * num2
        elif ops == 'divide':
            result = num1 / num2

    # Render the result template
    return jsonify(result)







if __name__=="__main__":
    app.run(host="0.0.0.0")
