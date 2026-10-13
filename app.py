from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy #Essa parte prepara/importa as ferramentas vão ser usadas

app = Flask(__name__) # "Liga" o petshop

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/petshop'
db = SQLAlchemy(app) #  Aqui acontece a conexão com o banco de dados "pets.db"

# Aqui cria a ligação, diz que um tutor pode ter vários Pets.
class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), nullable=False) # CPF do tutor
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False) # E-mail do tutor
# O 'backref="dono"' cria um atalho. Depois, no HTML, a gente pode usar "pet.dono.nome".
    pets = db.relationship('Pet', backref='dono', lazy=True)

# Aqui abaixo a gente cria a tabela no banco de dados (id, nome, especie, raca, sexo, kilos)
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    raca = db.Column(db.String(50), nullable=False)
    sexo = db.Column(db.String(20), nullable=False)
    kilos = db.Column(db.Float, nullable=False)
    
# Agora está como nullable=True para o pet não ser apagado ou dar erro 
# caso o tutor seja excluído do sistema, mantendo o historico do pet.
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id'), nullable=True)

# Isso aqui cria as tabelas no banco de dados
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
        tutor_id = request.form.get('tutor_id') # Pega o dono que escolhemos na caixinha
        
        # Cria um pacote com os dados que a gente digitou e salva
        novo_pet = Pet(nome=nome_pet, especie=especie_pet, raca=raca_pet, sexo=sexo_pet, kilos=float(kilos_pet), tutor_id=tutor_id) # NOVO: Salva o tutor_id junto
        db.session.add(novo_pet)
        db.session.commit()
        
        return redirect(url_for('inicio'))
    
    # pega todos os pets do banco de dados pra mostrar no html
    lista_pets = Pet.query.all()
    lista_tutores = Tutor.query.all() # aqui busca os tutores para mostrar na caixinha de seleção
    
    #Envia também a lista_tutores para o HTML
    return render_template('index.html', pets=lista_pets, tutores=lista_tutores)

@app.route('/deletar/<int:id>')
def deletar(id):
    # busca o pet pelo id e apaga
    pet = Pet.query.get(id)
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    pet = Pet.query.get_or_404(id)
    lista_tutores = Tutor.query.all() # Busca os tutores para permitir alterar o dono na edição
    
    if request.method == 'POST':
        # atualiza com os dados novos que vieram do html
        pet.nome = request.form.get('nome')
        pet.especie = request.form.get('especie')
        pet.raca = request.form.get('raca')
        pet.sexo = request.form.get('sexo')
        pet.kilos = float(request.form.get('kilos'))
        pet.tutor_id = request.form.get('tutor_id') # Atualiza o tutor na edição
        
        db.session.commit()
        return redirect(url_for('inicio'))
        
    return render_template('editar.html', pet=pet, tutores=lista_tutores)

@app.route('/tutores', methods=['GET', 'POST'])
def tutores():
    # Se o usuário clicou no botão de cadastrar (POST)
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf'] # Pega o CPF
        telefone = request.form['telefone']
        email = request.form['email'] # Pega o E-mail
        
        # Cria o tutor e salva no banco 
        novo_tutor = Tutor(nome=nome, cpf=cpf, telefone=telefone, email=email)
        db.session.add(novo_tutor)
        db.session.commit()
        
        return redirect(url_for('tutores')) # Recarrega a página
    
    # Se ele só está abrindo a página (GET), lista os tutores
    lista_tutores = Tutor.query.all()
    return render_template('tutores.html', tutores=lista_tutores)


# Aqui é para editar o dados do Tutor
@app.route('/editar_tutor/<int:id>', methods=['GET', 'POST'])
def editar_tutor(id):
    tutor = Tutor.query.get(id)
    
    if request.method == 'POST':
        tutor.nome = request.form.get('nome')
        tutor.cpf = request.form.get('cpf')
        tutor.telefone = request.form.get('telefone')
        tutor.email = request.form.get('email')
        
        db.session.commit()
        return redirect(url_for('tutores'))
        
    return render_template('editar_tutor.html', tutor=tutor)

# Aqui é para excluir o Tutor, mantendo os pets salvos
@app.route('/deletar_tutor/<int:id>')
def deletar_tutor(id):
    tutor = Tutor.query.get(id)
    
    # Antes de apagar o tutor, tiramos o vínculo dos pets dele (deixando o tutor_id como None/vazio)
    for pet in tutor.pets:
        pet.tutor_id = None
        
    db.session.delete(tutor)
    db.session.commit()
    return redirect(url_for('tutores'))

if __name__ == '__main__':
    app.run(debug=True)