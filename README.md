# django-online-test

É um sistema desenvolvido para facilitar a criação, gestão e resposta a simulados online. Com uma interface intuitiva, ele permite que usuários autenticados criem questões objetivas e organizem simulados personalizados, com diferentes níveis de dificuldade e pesos atribuídos a cada questão. O sistema visa atender tanto educadores quanto estudantes, fornecendo uma plataforma robusta e flexível para práticas de avaliação e estudo. Seja para fins acadêmicos ou para reforço de conhecimentos, o django-online-test se destaca por sua simplicidade e eficiência na geração de simulados de alta qualidade.

## Instalação

Para configurar e executar o projeto Django, siga os passos abaixo:

1. **Clonar o repositório**:

   Se ainda não o fez, clone o repositório do projeto para o seu ambiente local:
   ```bash
   git clone https://github.com/JoaoRobert0/django-online-test.git
   cd django-online-test
   ```

2. **Criar um ambiente virtual**:

   Para isolar as dependências do projeto, crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

3. **Ativar o ambiente virtual**:

   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar as dependências**:

   Com o ambiente virtual ativo, instale as dependências listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

   > **Nota**: As dependências incluem pacotes como `Django 5.1` e `sqlparse`. Certifique-se de que todos os pacotes foram instalados corretamente.

5. **Configurar o banco de dados**:

   Realize as migrações iniciais para configurar o banco de dados:
   ```bash
   python manage.py migrate
   ```

6. **Criar um superusuário (opcional)**:

   Se desejar acessar a interface administrativa do Django, crie um superusuário:
   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar o servidor de desenvolvimento**:

   Finalmente, inicie o servidor local para testar o projeto:
   ```bash
   python manage.py runserver
   ```

   O projeto estará disponível em [http://localhost:8000](http://localhost:8000).

8. **Acessar a interface administrativa (opcional)**:

   Se criou o superusuário, acesse a interface administrativa em [http://localhost:8000/admin](http://localhost:8000/admin) e faça login com as credenciais que você criou.

Agora você está pronto para desenvolver ou testar o sistema de simulados online!

## Documentação
[Link para os documentos do projeto](docs/pt-BR/documentacao.md)