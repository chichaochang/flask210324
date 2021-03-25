from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def submit():
    if request.method == "POST":
        username = request.values['username']
        password = request.values['password']
        if username=='david' and password=='1234':
            return '歡迎光臨本網站！'
        else:
            return '帳號或密碼錯誤！'
    return """
            <form method='post' action=''>
                <p>帳號：<input type='text' name='username' /></p>
                <p>密碼：<input type='text' name='password' /></p>
                <p><button type='submit'>確定</button></p>
            </form>
    """


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/hello/<string:name>')
def hello03(name):
    now = datetime.now()
    return render_template('hello3.html', **locals())


@app.route('/variable')
def variable():
    student = {'學號':'874523', '姓名':'張三', '性別':'男'}
    fruit = ['蘋果', '香蕉', '芭樂', '百香果']
    return render_template('variable.html', **locals())


@app.route('/show')
def show():
    person1={"name":"Amy","phone":"049-1234567","age":20}
    person2={"name":"Jack","phone":"02-4455666","age":25}
    person3={"name":"Nacy","phone":"04-9876543","age":17}
    persons=[person1,person2,person3]
    return render_template('show.html', **locals())


if __name__ == '__main__':
    app.run()
