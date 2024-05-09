from flask import Flask, render_template, request

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

    
@app.route('/inverter', methods=['POST'])
def inverter():
    n = request.form['n']
    mensagem = (n[::-1])
    return render_template('index.html', msg=mensagem)

if (__name__) == ('__main__'):
    app.run(debug=True)