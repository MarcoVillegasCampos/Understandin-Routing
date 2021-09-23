from flask import Flask, render_template


app= Flask( __name__)



dictionary={}

@app.route('/', methods=['GET'])
def loadHome():
    return "Hello World!"

@app.route('/dojo', methods=['GET'])
def loaddojo():
    return "Dojo!"

@app.route('/say/<some_word>', methods=['GET'])
def loadSay(some_word):
    
    return "Hi "+ str(some_word)+"!"

@app.route('/repeat/<times>/<word>', methods=['GET'])
def repeatHello(times,word):
    someWord=""
    for i in range(0,int(times)):
        someWord+=str(word)+"<br/>"    
    return someWord








if __name__ == "__main__":
    app.run(debug=True)
    