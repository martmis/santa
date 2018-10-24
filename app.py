from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def santa_form():
    return render_template("index.html")


@app.route('/result',methods = ['POST', 'GET'])
def result():
    try:
        name = request.form['name']
        mail = request.form['mail']

        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO santas (name,mail) VALUES(?, ?)", (name, mail))

            con.commit()
            msg = "Record successfully added"
    except:
        con.rollback()
        msg = "error in insert operation"

    finally:
        return render_template("result.html", msg=msg)
        con.close()


if __name__ == '__main__':
    app.run()
