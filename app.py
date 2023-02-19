from flask import Flask, render_template, request

from . import hebrew_arabic_transliteration
from translation_map import translations, clusters, sofit_forms, second_pass


app = Flask(__name__)

@app.route("/transliterate")
def translate():
    return render_template('translate.html')

@app.route("/result", methods=['POST'])
def result():
    text = request.form['text']
    result = hebrew_arabic_transliteration.process_words(
                text,
                translations,
                clusters,
                sofit_forms,
                second_pass)

    return render_template('result.html', result=result)