from flask import Flask, render_template, request
app = Flask(__name__)
print(__name__)

@app.route('/a')
def hello_world():
    return 'Welcome!!, World!!!'

@app.route('/')
def hello():
    return render_template('index.html')

def write_to_file(data):
    f = open('database.txt',mode='a',newline='')
    email=data['email']
    subject=data['text']
    message=data['message']
    f.write(f'{email} , {subject} , {message}\n')

@app.route('/submit_form',methods=['Post','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            return 'thank you!, I will check the message.'
        except exception as e:
            print(e)
            return 'something went wrong while saving data'
    else:
        return 'something went wrong'
