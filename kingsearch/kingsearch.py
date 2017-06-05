# all the imports
import os
import sqlite3
from flask import Flask, jsonify, json, request

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

app.config.from_envvar('KINGSEARCH_SETTINGS', silent=True)

@app.route('/', methods=['POST'])
def index():
    try:
        query = request.form['query']
        king_file = open('king-i-150.txt')
        king_text = king_file.read()
        king_file.close()

        results_dict = {
            'query_text': query,
            'number_of_occurrences': len(search_result),
            'occurrences': search_result}

    except Exception as err:
        print("Error: {0}".format(err))
        return jsonify({'Error': "{0}".format(err)})

    return jsonify(results_dict)

def search_text(pat, txt=None):
    occurences = []
    for i, line in enumerate(txt.splitlines()):
        line_result = search_line(pat, line, i + 1)
        if line_result is not None:
            occurences.extend(line_result)
    return occurences

def search_line(pat, txt, line):
    size = len(pat)
    occ = []
    for i in range(len(txt) -size + 1):
        if txt[i : i + size] == pat:
            occ.append({
                'line': line,
                'start': i + 1,
                'end': i + 1 + size})
    if len(occ) is 0:
        return None
    return occ
