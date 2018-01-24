from flask import Flask, render_template, request
from modified_diff import textDiff
app = Flask(__name__)


@app.route('/')
def upl_file():
    return render_template('index.html')


@app.route('/differ', methods=['POST'])
def upload_file():
    first_file = request.files['inputFirstFile']
    second_file = request.files['inputSecondFile']
    first_data = first_file.readlines()
    second_data = second_file.readlines()
    first_html_list = [first_row.decode('utf-8', 'ignore') for
                       first_row in first_data]
    second_html_list = [second_row.decode('utf-8', 'ignore') for
                        second_row in second_data]
    differents = textDiff(first_html_list, second_html_list)
    return render_template('differ.html', differents=differents,
                           first_html_list=first_html_list,
                           second_html_list=second_html_list)


if __name__ == '__main__':
    app.run()
