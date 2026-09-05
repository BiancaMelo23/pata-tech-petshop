from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy #(Essa parte prepara/importa as ferramentas que serão usadas)

app = Flask(__name__) # ("Liga" o petshop)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
db = SQLAlchemy(app) # ( Aqui acontece a conexão com o banco de dados "pets.db")

# Aqui abaixo a gente cria a tabela no banco de dados (id, nome, especie, raca, sexo, kilos)
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(100), nullable=False)
    raca = db.Column(db.String(100), nullable=False)
    sexo = db.Column(db.String(20), nullable=False)
    kilos = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all() # aqui transforma o id(numero de identificação ) em algo existente em nosso computador)

@app.route('/', methods=['GET', 'POST']) #essa parte o código cria a página inicial e verifica se o usuário apenas entrou nela ou se enviou alguma coisa.
def inicio():
    if request.method == 'POST':
       
        
        # Pega os dados que a gente digita
        nome_pet = request.form.get('nome')
        especie_pet = request.form.get('especie')
        raca_pet = request.form.get('raca')
        sexo_pet = request.form.get('sexo')
        kilos_pet = request.form.get('kilos')
        
       
        # Cria um pacote com os dados que a gente digitou e salva
        novo_pet = Pet(nome=nome_pet, especie=especie_pet, raca=raca_pet, sexo=sexo_pet, kilos=float(kilos_pet))
        db.session.add(novo_pet)
        db.session.commit()
        
        return redirect(url_for('inicio'))
    
    # pega todos os pets do banco de dados pra mostrar no html
    lista_pets = Pet.query.all()
    return render_template('index.html', pets=lista_pets)

@app.route('/deletar/<int:id>')
def deletar(id):
    # busca o pet pelo id e apaga
    pet = Pet.query.get(id)
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    pet = Pet.query.get(id)
    
    if request.method == 'POST':
        # atualiza com os dados novos que vieram do html
        pet.nome = request.form.get('nome')
        pet.especie = request.form.get('especie')
        pet.raca = request.form.get('raca')
        pet.sexo = request.form.get('sexo')
        pet.kilos = float(request.form.get('kilos'))
        
        db.session.commit()
        return redirect(url_for('inicio'))
        
    return render_template('editar.html', pet=pet)

if __name__ == '__main__':
    app.run(debug=True)