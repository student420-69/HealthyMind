from django.shortcuts import render
from flask import Flask, redirect, session, url_for, render_template, request, flash, redirect
from flask_mysqldb import MySQL
import re

app = Flask(__name__)
#Conexion MYSQL
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "mydb"
mysql = MySQL(app)
#Inicializar sesion
app.secret_key = 'healthyMindSecret'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encuesta")
def encuesta():
    return render_template("encuesta.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/color")
def color():
    return render_template("color.html")

@app.route("/depresion")
def depresion():
    return render_template("Depresion.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/resultadoMinimo")
def resultadoMinimo():
    return render_template("resultadoMin.html")

@app.route("/resultadoLeve")
def resultadoLeve():
    return render_template("resultadoLeve.html")

@app.route("/resultadoModerado")
def resultadoModerado():
    return render_template("resultadoMod.html")

@app.route("/resultadoGrave")
def resultadoGrave():
    return render_template("resultadoGrave.html")

@app.route("/terminosRegistro")
def terminosRegistro():
    return render_template("TerConReg.html")

@app.route("/terminosResultado")
def terminosResultado():
    return render_template("terminosResul.html")

@app.route('/colorSend', methods=['GET', 'POST'])
def colEnviar():
    if request.method == "POST":
        colorfav = request.form.get("color_fav")
        session["colorfav"] = colorfav
        return redirect(url_for('registro'))

@app.route('/registroSend', methods=['GET', 'POST'])
def regEnviar():
    if request.method == "POST":
        error = 0
        regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        regexNombre = r'([a-zA-Z])\D*([a-zA-Z])$'
        nombre = request.form.get("nombre")
        email = request.form.get("correo")
        if len(email) == 0:
            cur1 = mysql.connection.cursor()
            cur1.execute("SELECT idpeople FROM people ORDER BY idpeople DESC LIMIT 1")
            ultimo_id = cur1.fetchall()
            email = "-00"+str(ultimo_id)
        edad = request.form.get("edad")
        edad = int(edad)
        genero = request.form.get("genero")
        pronombre = request.form.get("pronombre")
        colorFav = session["colorfav"]
        session["nombre"] = nombre
        session["email"] = email
        session["edad"] = edad
        session["genero"] = genero
        session["pronombre"] = pronombre
        if len(nombre) > 1 and not re.fullmatch(regexNombre, nombre):
            flash("Nombre contiene caracteres invalidos")
            error+=1
        if len(email) > 1 and not re.fullmatch(regexEmail, email) and not email.startswith("-00"):
            flash("Correo electronico Invalido")
            error+=1
        if edad < 18 or edad > 90:
            flash("Edad Invalida")
            error+=10
        if genero == "":
            flash("Selecciona un genero con el que te identificas")
            error+=1
        if not pronombre == "El" and not pronombre == "Ella" and not pronombre == "Elle" and not pronombre == "Nosotres":
            flash("Selecciona un pronombre dentro de la lista ofrecida")
            error+=1
        if error == 0:
            cur = mysql.connection.cursor()
            if len(nombre) == 0:
                cur.execute("INSERT INTO people (edad,colorFav,genero,email,pronombre) VALUES (%s,%s,%s,%s,%s)",(edad,colorFav,genero,email,pronombre))
            else:
                cur.execute("INSERT INTO people (nombre,edad,colorFav,genero,email,pronombre) VALUES (%s,%s,%s,%s,%s,%s)",(nombre,edad,colorFav,genero,email,pronombre))
            mysql.connection.commit()
            session["id"] = cur.lastrowid
            return redirect(url_for('terminosRegistro'))
        elif error >= 10:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('error'))

@app.route('/encuestaSend', methods=['GET', 'POST'])
def encEnviar():
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur1 = mysql.connection.cursor()
        error = 0
        if request.form.get("p1") == None or request.form.get("p2") == None or request.form.get("p3") == None or request.form.get("p4") == None or request.form.get("p5") == None:
            error+=1
        elif request.form.get("p6") == None or request.form.get("p7") == None or request.form.get("p8") == None or request.form.get("p9") == None or request.form.get("p10") == None:
            error+=1
        elif request.form.get("p11") == None or request.form.get("p12") == None or request.form.get("p13") == None or request.form.get("p14") == None or request.form.get("p15") == None:
            error+=1
        elif request.form.get("p16") == None or request.form.get("p17") == None or request.form.get("p18") == None or request.form.get("p19") == None or request.form.get("p20") == None or request.form.get("p21") == None:
            error+=1
        if error > 0:
            flash("Verifica que todas las preguntas hayan sido respondidas")
            return redirect(url_for('error'))
        else:
            resultado = int(request.form.get("p1"))
            resultado += int(request.form.get("p2"))
            resultado += int(request.form.get("p3"))
            resultado += int(request.form.get("p4"))
            resultado += int(request.form.get("p5"))
            resultado += int(request.form.get("p6"))
            resultado += int(request.form.get("p7"))
            resultado += int(request.form.get("p8"))
            resultado += int(request.form.get("p9"))
            resultado += int(request.form.get("p10"))
            resultado += int(request.form.get("p11"))
            resultado += int(request.form.get("p12"))
            resultado += int(request.form.get("p13"))
            resultado += int(request.form.get("p14"))
            resultado += int(request.form.get("p15"))
            resultado += int(request.form.get("p16"))
            resultado += int(request.form.get("p17"))
            resultado += int(request.form.get("p18"))
            resultado += int(request.form.get("p19"))
            resultado += int(request.form.get("p20"))
            resultado += int(request.form.get("p21"))
            session["resultadoP"] = resultado
        if resultado >= 0 and resultado <= 13:
            session["diagnostico"] = "Depresion Minima"
            cur.execute("INSERT INTO result (idpeople,idquestionnaire,testResultado) VALUES (%s,%s,%s)",(session["id"],1,session["diagnostico"]))
            mysql.connection.commit()
            session["idRes"] = cur.lastrowid
            cur1.execute("INSERT INTO response (idpeople, idquestionnaire, idresultado, respuesta) VALUES(%s, %s, %s, %s)",(session["id"],1,session["idRes"],session["resultadoP"]))
            mysql.connection.commit()
            return redirect(url_for('resultadoMinimo'))
        elif resultado >= 14 and resultado <= 19:
            session["diagnostico"] = "Depresion Leve"
            cur.execute("INSERT INTO result (idpeople,idquestionnaire,testResultado) VALUES (%s,%s,%s)",(session["id"],1,session["diagnostico"]))
            mysql.connection.commit()
            session["idRes"] = cur.lastrowid
            cur1.execute("INSERT INTO response (idpeople, idquestionnaire, idresultado, respuesta) VALUES(%s, %s, %s, %s)",(session["id"],1,session["idRes"],session["resultadoP"]))
            mysql.connection.commit()
            return redirect(url_for('resultadoLeve'))
        elif resultado >= 20 and resultado <= 28:
            session["diagnostico"] = "Depresion Moderada"
            cur.execute("INSERT INTO result (idpeople,idquestionnaire,testResultado) VALUES (%s,%s,%s)",(session["id"],1,session["diagnostico"]))
            mysql.connection.commit()
            session["idRes"] = cur.lastrowid
            cur1.execute("INSERT INTO response (idpeople, idquestionnaire, idresultado, respuesta) VALUES(%s, %s, %s, %s)",(session["id"],1,session["idRes"],session["resultadoP"]))
            mysql.connection.commit()
            return redirect(url_for('resultadoModerado'))
        else:
            session["diagnostico"] = "Depresion Grave"
            cur.execute("INSERT INTO result (idpeople,idquestionnaire,testResultado) VALUES (%s,%s,%s)",(session["id"],1,session["diagnostico"]))
            mysql.connection.commit()
            session["idRes"] = cur.lastrowid
            cur1.execute("INSERT INTO response (idpeople, idquestionnaire, idresultado, respuesta) VALUES(%s, %s, %s, %s)",(session["id"],1,session["idRes"],session["resultadoP"]))
            mysql.connection.commit()
            return redirect(url_for('resultadoGrave'))
        

if __name__ == "__main__":
    app.run()
 