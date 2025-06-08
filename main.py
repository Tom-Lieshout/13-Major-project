from flask import Flask
from flask import render_template

app = Flask('__name__')


@app.route('/main')
def main():
    return render_template("main.html", name=main)



if __name__ == "__main__":
    app.run(debug=True)
    print("hello world")
    