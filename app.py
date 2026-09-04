# Importando as ferramentas necessárias do Flask e do Banco de Dados
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Inicializando o aplicativo do Flask
app = Flask(__name__)

# Configurando o endereço do nosso banco de dados local (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definindo a estrutura da tabela 'Pet' no banco de dados (nossas colunas)
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Identificador único
    nome = db.Column(db.String(100), nullable=False) # Nome do animal
    especie = db.Column(db.String(100), nullable=False) # Espécie (Gato, Cachorro, etc.)
    sexo = db.Column(db.String(20), nullable=False) # NOVO: Sexo do animal
    kilos = db.Column(db.Float, nullable=False) # Peso do pet

# Criando o banco de dados e a tabela automaticamente
with app.app_context():
    db.create_all()

# Rota principal (Página Inicial): Mostra a lista e cadastra
@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        nome_pet = request.form.get('nome')
        especie_pet = request.form.get('especie')
        sexo_pet = request.form.get('sexo') # Puxando o sexo do formulário
        kilos_pet = request.form.get('kilos')
        
        # Cria um novo objeto Pet incluindo o sexo
        novo_pet = Pet(nome=nome_pet, especie=especie_pet, sexo=sexo_pet, kilos=float(kilos_pet))
        db.session.add(novo_pet)
        db.session.commit()
        
        return redirect(url_for('inicio'))
    
    lista_pets = Pet.query.all()
    return render_template('index.html', pets=lista_pets)

# Rota para DELETAR
@app.route('/deletar/<int:id>')
def deletar(id):
    pet = Pet.query.get_or_404(id)
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for('inicio'))

# Rota para EDITAR
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    pet = Pet.query.get_or_404(id)
    
    if request.method == 'POST':
        pet.nome = request.form.get('nome')
        pet.especie = request.form.get('especie')
        pet.sexo = request.form.get('sexo') # Atualiza o sexo
        pet.kilos = float(request.form.get('kilos'))
        db.session.commit()
        return redirect(url_for('inicio'))
        
    return render_template('editar.html', pet=pet)

if __name__ == '__main__':
    app.run(debug=True)