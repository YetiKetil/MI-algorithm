import os
from flask import Flask, request, render_template, flash, redirect, url_for, send_file, send_from_directory
from webapp.app import app
from webapp.app.forms import SimilarityForm, SimilarityFormPaste
from werkzeug.utils import secure_filename

from logic.text_manipulation import text_manipulation

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['txt', 'csv'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16MB file size is max

tm = text_manipulation(app.config['UPLOAD_FOLDER'])


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/simple_test', methods=['GET', 'POST'])
def simple_test():
    """
    Function reads two string from the form and calculates the similarity
    :return: Text and similarity number are rendered on the page
    """
    form = SimilarityForm()
    text = ""
    if request.method == 'POST':
        text1 = str(form.text1.data)
        text2 = str(form.text2.data)
        text = tm.simple_two_text_analysis(text1, text2)

    return render_template('simple_test.html', form=form, text=text)


@app.route('/compare_paste', methods=['GET', 'POST'])
def compare_paste():
    """
    Compares sentences pasted in the textbox
    :return:
    """
    form = SimilarityFormPaste()
    text = ""
    if request.method == 'POST':

        all_text = str(form.text_box.data)
        tm.analysis_from_pasted_text(all_text)
        text = "Text similarity analysis is done!"

    return render_template('compare_paste.html', form=form, text=text)

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
        return send_file(tm.save_file_full_path, attachment_filename=tm.save_filename)
    except Exception as e:
        return str(e)

# Upload

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/compare_file', methods=['GET', 'POST'])
def compare_file():
    print("request.method:", request.method)
    text = ""
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

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            tm.analysis_from_file(filename)

        text = "Text similarity analysis is done!"
    return render_template('compare_file.html', text = text)

"""
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
"""

"""
@app.route('/result/<text>')
def result(text):
    text = tm.text_analysis(text)
    return render_template('result.html', text=text)
"""