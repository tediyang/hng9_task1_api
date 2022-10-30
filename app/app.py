import os
from flask import Flask
import json

app = Flask(__name__)
DEPLOY = os.getenv('DEPLOY')

@app.route('/', methods=['GET'])
def home_page():
    my_data = {'slackUsername': 'Eyang, Daniel Eyoh', \
        'backend': True, 'age': 26, \
        'bio': "I'm Eyang, Daniel Eyoh, an Entry Backend \
        Software and Machine Learning Engineer (Python)  \
        who loves building models and computer software. \
        I'm working on an app using CNN that let users get \
        the names of cars' Images and legal locations where they can purchase them. \
        Despite having a B.Sc. degree in Geology, I combined my passion for learning \
        and development, channelled it to Data Science & Software Development and acquired\
        skills which helps me in building personalized software for people."}
    json_dump = json.dumps(my_data)

    return json_dump

if __name__ == '__main__':
    app.run(debug=True)
