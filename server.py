from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)
    # Create a new instance of the Flask class called "app"
@app.route('/play')  
def play():
    return render_template('index.html',num=3,color="blue")

@app.route('/play/<int:num>')
def play2(num):
    return render_template('index.html',num=num,color="blue")

@app.route('/play/<int:num>/<string:color>')
def play3(num,color):
    return render_template('index.html',num=num,color=color)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    