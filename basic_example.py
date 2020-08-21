__author__ = 'RD'

import flask
import pandas as pd
from flask import Flask, render_template, request
from searchData import searchData
html = """
<! DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF-8">
    <title>DataFrame display test</title>
</head>
<body>
{{table | safe}}
</body>
</html>
"""
app = Flask(__name__)
@ app.route ('/')

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    output = searchData(first_name)
    return flask.render_template_string (html, table = output.to_html (header = 'true'))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)

# import flask
# import pandas as pd
# from flask import Flask, render_template, request
# from searchData import searchData
# html = """
# <! DOCTYPE html>
# <html lang = "en">
# <head>
#     <meta charset = "UTF-8">
#     <title>DataFrame display test</title>
# </head>
# <body>
# {{table | safe}}
# </body>
# </html>
# """
# app = Flask(__name__)
# @ app.route ('/')
# def index ():
#     df = pd.DataFrame ({'key': ['A', 'B', 'C', 'D', 'E', 'F'],
#                        'val': [0.09,0.1,0.8,0.2,0.7,0.1]})
#     return flask.render_template_string (html, table = df.to_html (header = 'true'))
# if __name__ == '__main__':
#     app.run (debug = True)