'''Import necessary files'''
from flask import Flask, request

app = Flask(__name__)


# @app.route('/', methods=['GET'])
# def home_page():
#     '''Get request taking you directly to homepage'''
@app.route('/', methods=['POST', 'GET'])
def home_page_post():
    '''Post request taking you directly to homepage'''
    if request.method == 'POST':
        x_value = request.get_json('x', type=int)
        y_value = request.get_json('y', type=int)
        operand = request.get_json('operation_type')
        for i in operand:
            if i in ('subtraction', 'subtract'):
                z_value = x_value - y_value
                operand = i
                break
            if i in ('addition', 'add'):
                z_value = x_value + y_value
                operand = i
                break
            if i in ('multiplication', 'multiply'):
                z_value = x_value * y_value
                operand = i
                break
        my_data = { 'slackUsername': 'Eyang, Daniel Eyoh',
                'result': z_value, 'operation_type': operand}
        return my_data

    if request.method == 'GET':
        my_data = {'slackUsername': 'Eyang, Daniel Eyoh',
                   'backend': True, 'age': 26,
                   'bio': "I'm Eyang, Daniel Eyoh, an Entry Backend Software and Machine Learning Engineer (Python) who loves building models and computer software. I'm working on an app using CNN that let users get the names of cars' Images and legal locations where they can purchase them. Despite having a B.Sc. degree in Geology, I combined my passion for learning and development, channelled it to Data Science & Software Development and acquired skills which helps me in building personalized software for people."}
        return my_data


if __name__ == '__main__':
    app.run(debug=True)
