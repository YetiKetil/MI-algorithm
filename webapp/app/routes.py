import os
from flask import Flask, request, render_template, flash, redirect, url_for, send_file, send_from_directory
from webapp.app import app
from webapp.app.forms import SimilarityForm
from werkzeug.utils import secure_filename

import csv

from logic.sentsim_mihalcea_bnc import MihalceaSentSimBNC

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['txt', 'csv'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16MB file size is max

filename = ""
save_filename = ""
save_file_full_path = ""

#########################
## text similarity logic
#########################

def read_from_file(file):
    """
    Function reads whole content from a file and puts it in a string
    :param file: full path to the file
    :return: whole text from file as a string
    """
    print("PATH TO READ FILE:" + file)
    whole_text = ""
    with open(file) as f:
        read_obj = csv.reader(f)
        for row in read_obj:
            whole_text += '\n'.join(row)
            #whole_text += "\n"
    print(whole_text)
    return whole_text

def save_to_file(text):
    global save_filename
    if len(filename) != 0:
        save_filename = filename.replace(".", "_result.")
    else:
        save_filename = "manual_result.csv"
    global save_file_full_path
    save_file_full_path = UPLOAD_FOLDER + "/" + save_filename

    text = text.replace("\n", "\t")# prepare text as tab delimited

    f = open(save_file_full_path, 'wt', encoding='utf-8')
    f.write(text)
    f.close()

def text_analysis(text_analysis):
    """
    :param text_analysis:
    :return:
    """
    sentsim = MihalceaSentSimBNC()
    sentsim.download_nltk_resources()

    print("TEXT FOR ANALYSIS:")
    print(text_analysis)
    print("***********************************")
    list_text = text_analysis.split("\n")
    text_1 = list_text[0]
    text_2 = list_text[1]

    score = round(sentsim.similarity(text_1, text_2), 4)

    text_analysis = text_analysis + "\n" + str(score)

    save_to_file(text_analysis)
    text_analysis = text_analysis.replace('\n', '<br>')

    return text_analysis

############################
##END text similarity logic
############################

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/result/<text>')
def result(text):
    text = text_analysis(text)
    return render_template('result.html', text=text)


@app.route('/compare', methods=['GET', 'POST'])
def compare():
    form = SimilarityForm()
    text = str(form.text1.data) + "\n" + str(form.text2.data)
    if form.validate_on_submit():
        #return redirect(url_for('result', text1=form.text1.data, text2=form.text2.data))
        return redirect(url_for('result', text=text))
    return render_template('compare.html', form=form)


# Download

@app.route('/file-downloads')
def file_downloads():
    try:
        return render_template('result.html')
    except Exception as e:
        return str(e)


@app.route('/download')
def download():
    try:
        return send_file(save_file_full_path, attachment_filename=save_filename)
    except Exception as e:
        return str(e)

# Upload

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/compare_file', methods=['GET', 'POST'])
def compare_file():
    print("request.method:", request.method)
    if request.method == 'POST':
        print("compare_file - POST")
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            global filename
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            text_from_file = read_from_file(str(app.config['UPLOAD_FOLDER']) + "/" + filename)

            #text = text_analysis(text_from_file)
            return redirect(url_for('result', text=text_from_file))
            #return redirect(url_for('uploaded_file', filename=filename))

    return render_template('compare_file.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

