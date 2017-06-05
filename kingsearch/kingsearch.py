# all the imports
import os
import nltk
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

        search_result = search_text(query, king_text)
        # search_result = extract_sentances(king_text, search_result, query)

        # tokenizer = nltk.data.load('nltk:tokenizers/punkt/PY3/english.pickle')
        tokens = nltk.word_tokenize(king_text)
        text = nltk.Text(tokens)
        # sentences = nltk.sent_tokenize(king_text)
        # sentences = [nltk.word_tokenize(sent) for sent in sentences]
        # sentences = [nltk.pos_tag(sent) for sent in sentences]
        print(text.concordance(query))

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

# def extract_sentances(txt, results, query):
#     for occurence in results:
#         occurence['in_sentence'] = find_sentance(occurence, txt, query)
#     return results

# def find_sentance(occurence, txt):
