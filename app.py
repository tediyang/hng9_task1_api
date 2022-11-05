'''Import necessary files'''
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['POST', 'GET'])
def home_page_post():
    '''Check requests'''
    if request.method == 'POST':
        result = 0

        #variaties of operands
        lis = ['+', '-', '*', 'addition', 'subtraction',
         'multiplication', 'add', 'subtract', 'multiply', 'product']

        #Get the json request data
        data = request.get_json()
        opera = data.get("operation_type")
        x_value = data.get("x")
        y_value = data.get("y")

        #Split the opertion field to check if it is a string of different operands"""
        spli = ""
        try:
            spli = opera.split(' ')
        except TypeError:
            pass

        if len(spli) > 1:
            for i in spli:
                if i in lis:
                    opera = i
                    break

        # Validate the input and perform action"""
        if (isinstance(y_value, int) and isinstance(x_value, int) and opera):
            if opera in (lis[0], lis[3], lis[6]):
                result = x_value + y_value
            elif opera in [lis[1], lis[4], lis[7]]:
                result = x_value - y_value
            elif opera in [lis[2], lis[5], lis[8], lis[9]]:
                result = x_value * y_value
            return ({"slackUsername": 'Eyang, Daniel Eyoh',
                    "operation_type": opera,
                    "result": result})

    if request.method == 'GET':
        data = {'slackUsername': 'Eyang, Daniel Eyoh',
                    'backend': True, 'age': 26,
                    'bio': "I'm Eyang, Daniel Eyoh, an Entry Backend Software and Machine Learning Engineer (Python) who loves building models and computer software. I'm working on an app using CNN that let users get the names of cars' Images and legal locations where they can purchase them. Despite having a B.Sc. degree in Geology, I combined my passion for learning and development, channelled it to Data Science & Software Development and acquired skills which helps me in building personalized software for people."}

        return data

    return "Wrong format"


if __name__ == '__main__':
    app.run(debug=True)
    