from flask import Flask, render_template, request, jsonify
from flask import send_from_directory
import random
import string
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/generate', methods=['POST'])
def generate():
    # フォームデータを取得
    options = request.form.getlist('options')
    min_value = int(request.form['min-value'])
    max_value = int(request.form['max-value'])
    pattern_count = int(request.form['pattern-count'])

    # 使用する文字セットを選択
    char_set = ''
    if 'half-width-numbers' in options:
        char_set += string.digits  # 半角数字
    if 'full-width-numbers' in options:
        char_set += '０１２３４５６７８９'  # 全角数字
    if 'half-width-alphabets' in options:
        char_set += string.ascii_letters  # 半角英字
    if 'full-width-alphabets' in options:
        char_set += 'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ' \
                    'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ'  # 全角英字
    if 'full-width-characters' in options:
        char_set += 'あいうえおかきくけこさしすせそ'  # 全角文字 (例)
    if 'symbols' in options:
        char_set += '!@#$%^&*()_+'  # 記号

    # ランダムデータ生成
    random_data = []
    for _ in range(pattern_count):
        if char_set:
            value = ''.join(random.choice(char_set) for _ in range(random.randint(min_value, max_value)))
        else:
            value = ''
        random_data.append([value])

    # テキストファイルの生成と保存
    file_path = 'output.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        for value in random_data:
            file.write(','.join(value) + '\n')  # カンマ区切りのテキストとして保存

    # ファイルのダウンロードリンクを返す
    return jsonify({'links': [{'url': file_path, 'format': 'TXT'}]})

@app.route('/download/<filename>')
def download_file(filename):
    directory = os.getcwd()  # またはファイルが保存されているディレクトリ
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
