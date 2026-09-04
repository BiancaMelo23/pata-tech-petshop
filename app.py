from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Tabela atualizada com o campo 'kilos'
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(100), nullable=False)
    kilos = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        nome_pet = request.form.get('nome')
        especie_pet = request.form.get('especie')
        kilos_pet = request.form.get('kilos')
        
        # Salva o pet com o peso convertido para número
        novo_pet = Pet(nome=nome_pet, especie=especie_pet, kilos=float(kilos_pet))
        db.session.add(novo_pet)
        db.session.commit()
        
        return redirect(url_for('inicio'))
    
    lista_pets = Pet.query.all()
    return render_template('index.html', pets=lista_pets)

if __name__ == '__main__':
    app.run(debug=True)