from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    aluno = {
        "nome": "felipe farias",
        "turma": "2° ensino medio tecnico"
    }

    professores = [
        {
            "nome": "felipe ishara"
            "materia": "web"
        },
            {
                "nome": "edidio"
                "materia": "software"
            }
    ]


    return render_template('index.html', title= "lome")

@app.route("/boletim")
def boletim():
    return render_template('boletim.html', title= "boletim")



