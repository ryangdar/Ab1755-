__author__ = 'RD'

import flask
import pandas as pd
from flask import Flask, render_template, request
from searchData import searchData

html = """
<! DOCTYPE html>
<html lang = "en">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.21/css/jquery.dataTables.min.css">
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.3.1/semantic.min.css">
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.21/css/dataTables.semanticui.min.css">
<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.21/js/jquery.dataTables.js"></script>
<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js"></script>
<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.21/js/dataTables.semanticui.min.js"></script>
<script type="text/javascript" charset="utf8" src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.3.1/semantic.min.js"></script>
<script>
$(document).ready( function () {
    $('#my_id').DataTable();
} );
</script>
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
    return flask.render_template_string (html, table = output.to_html (header = 'true', classes =['ui celled table','hover'], table_id = 'my_id', render_links=True))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)

