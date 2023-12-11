from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-log-summarize1', methods=['POST'])
def run_log_summarize1():
    # ここで Log.py を実行する処理を書く
    return {"message": "Log.py 実行完了"}

@app.route('/open-log-summarize2')
def open_log_summarize2():
    # ここで "ログ集計.xlsm" ファイルをクライアントに提供する
    return send_file("path/to/ログ集計.xlsm", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)