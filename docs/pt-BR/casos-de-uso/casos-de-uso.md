# Casos de Uso

## Introdução

Este documento descreve os casos de uso para o sistema de gerenciamento e resposta a simulados online. Cada caso de uso detalha as interações entre os usuários e o sistema, visando atender às principais necessidades e funcionalidades descritas no Documento de Visão.

## Casos de Uso

### 1. Cadastro de Questões

**Descrição:** Permite que o moderador cadastre novas questões objetivas no sistema.

- **Ator Primário:** Moderador
- **Pré-condições:** O moderador deve estar autenticado no sistema.
- **Fluxo Principal:**
  1. O moderador acessa a interface de cadastro de questões.
  2. O sistema exibe um formulário para inserir o enunciado da questão.
  3. O moderador preenche o enunciado e adiciona as alternativas com a resposta correta.
  4. O moderador submete o formulário.
  5. O sistema valida as informações e salva a nova questão.
  6. O sistema confirma o cadastro bem-sucedido e exibe uma mensagem de sucesso.
- **Fluxos Alternativos:**
  - 3a. Se o moderador não preencher todos os campos obrigatórios, o sistema exibe mensagens de erro e solicita correções.
- **Pós-condições:** A nova questão é salva no banco de dados e está disponível para a criação de simulados.

### 2. Criação de Simulados

**Descrição:** Permite que o moderador crie simulados configurando questões e pesos associados a cada uma.

- **Ator Primário:** Moderador
- **Pré-condições:** O moderador deve estar autenticado no sistema e ter questões cadastradas.
- **Fluxo Principal:**
  1. O moderador acessa a interface de criação de simulados.
  2. O sistema exibe um formulário para criar um novo simulado.
  3. O moderador insere o nome e a descrição do simulado.
  4. O moderador seleciona as questões a serem incluídas no simulado e define os pesos para cada questão.
  5. O moderador configura as opções adicionais (tempo de resposta, número de tentativas, etc.).
  6. O moderador submete o formulário.
  7. O sistema valida as informações e salva o novo simulado.
  8. O sistema confirma a criação bem-sucedida e exibe uma mensagem de sucesso.
- **Fluxos Alternativos:**
  - 3a. Se o moderador não preencher todos os campos obrigatórios, o sistema exibe mensagens de erro e solicita correções.
- **Pós-condições:** O novo simulado é salvo no banco de dados e está disponível para o público geral.

### 3. Resolução de Simulados

**Descrição:** Permite que o visitante responda aos simulados disponíveis publicamente e visualize seus resultados.

- **Ator Primário:** Visitante
- **Pré-condições:** O visitante deve ter acesso à internet e um navegador web.
- **Fluxo Principal:**
  1. O visitante acessa a lista de simulados disponíveis.
  2. O sistema exibe a lista de simulados.
  3. O visitante seleciona um simulado para responder.
  4. O sistema exibe as questões do simulado.
  5. O visitante responde às questões e submete o simulado.
  6. O sistema avalia as respostas e gera um relatório de resultados.
  7. O sistema exibe o relatório de resultados para o visitante.
- **Fluxos Alternativos:**
  - 5a. Se o visitante não conseguir completar o simulado, o sistema salva o progresso e permite continuar posteriormente.
- **Pós-condições:** O visitante visualiza o resultado do simulado e tem a opção de revisar suas respostas.

### 4. Análise de Desempenho

**Descrição:** Fornece ao moderador ferramentas para monitorar e analisar o desempenho dos participantes nos simulados.

- **Ator Primário:** Moderador
- **Pré-condições:** O moderador deve estar autenticado no sistema e ter simulados com dados de participação.
- **Fluxo Principal:**
  1. O moderador acessa a interface de análise de desempenho.
  2. O sistema exibe uma lista de simulados e suas estatísticas de participação.
  3. O moderador seleciona um simulado para análise detalhada.
  4. O sistema exibe gráficos e relatórios sobre o desempenho dos participantes.
  5. O moderador revisa os dados e gera relatórios personalizados, se necessário.
- **Fluxos Alternativos:**
  - 4a. Se não houver dados suficientes para uma análise significativa, o sistema exibe uma mensagem informando sobre a falta de dados.
- **Pós-condições:** O moderador obtém relatórios e insights detalhados sobre o desempenho dos participantes.

### 5. Gerenciamento de Conteúdo

**Descrição:** Permite que o moderador gerencie e mantenha o conteúdo dos simulados e questões.

- **Ator Primário:** Moderador
- **Pré-condições:** O moderador deve estar autenticado no sistema.
- **Fluxo Principal:**
  1. O moderador acessa a interface de gerenciamento de conteúdo.
   2. O sistema exibe uma lista de questões e simulados existentes.
  3. O moderador seleciona o conteúdo a ser editado ou removido.
  4. O moderador realiza as alterações necessárias (editar, excluir, etc.).
  5. O sistema valida e salva as alterações.
  6. O sistema confirma as alterações e exibe uma mensagem de sucesso.
- **Fluxos Alternativos:**
  - 3a. Se o moderador tentar excluir um conteúdo associado a um simulado ativo, o sistema solicita confirmação antes da exclusão.
- **Pós-condições:** O conteúdo dos simulados e questões é atualizado conforme as modificações realizadas pelo moderador.

## Conclusão

Os casos de uso descritos abordam as principais funcionalidades do sistema, garantindo que as necessidades dos usuários sejam atendidas de forma eficaz. Cada caso de uso é projetado para proporcionar uma experiência intuitiva e eficiente, alinhada aos objetivos do projeto.
