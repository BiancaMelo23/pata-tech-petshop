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
    id = db.Column(db.Integer, primary_key=True) # Identificador único de cada pet
    nome = db.Column(db.String(100), nullable=False) # Nome do animal
    especie = db.Column(db.String(100), nullable=False) # Espécie (Gato, Cachorro, etc.)
    kilos = db.Column(db.Float, nullable=False) # Peso do pet em quilos

# Criando o banco de dados e a tabela automaticamente se não existirem
with app.app_context():
    db.create_all()

# Rota principal (Página Inicial): Mostra a lista e cadastra novos pets
@app.route('/', methods=['GET', 'POST'])
def inicio():
    # Se o usuário clicou no botão "Cadastrar Pet" (método POST)
    if request.method == 'POST':
        nome_pet = request.form.get('nome')
        especie_pet = request.form.get('especie')
        kilos_pet = request.form.get('kilos')
        
        # Cria um novo objeto Pet com os dados preenchidos
        novo_pet = Pet(nome=nome_pet, especie=especie_pet, kilos=float(kilos_pet))
        db.session.add(novo_pet) # Adiciona no banco
        db.session.commit() # Salva definitivamente
        
        # Recarrega a página limpa para mostrar o pet recém-cadastrado
        return redirect(url_for('inicio'))
    
    # Se for apenas acesso normal (método GET), busca todos os pets salvos
    lista_pets = Pet.query.all()
    # Envia a lista de pets para o arquivo HTML exibir na tela
    return render_template('index.html', pets=lista_pets)

# Rota para DELETAR um pet do banco de dados pelo ID dele
@app.route('/deletar/<int:id>')
def deletar(id):
    pet = Pet.query.get_or_404(id) # Procura o pet ou dá erro 404 se não achar
    db.session.delete(pet) # Deleta o registro
    db.session.commit() # Salva a alteração
    return redirect(url_for('inicio'))

# Rota para EDITAR os dados de um pet existente
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    pet = Pet.query.get_or_404(id) # Localiza o pet que queremos alterar
    
    # Se o usuário enviou o formulário de alteração preenchido
    if request.method == 'POST':
        pet.nome = request.form.get('nome')
        pet.especie = request.form.get('especie')
        pet.kilos = float(request.form.get('kilos'))
        db.session.commit() # Salva as atualizações no banco
        return redirect(url_for('inicio'))
        
    # Se apenas abriu a página de edição, mostra o formulário preenchido com os dados antigos
    return render_template('editar.html', pet=pet)

# Executando o servidor web localmente
if __name__ == '__main__':
    app.run(debug=True)