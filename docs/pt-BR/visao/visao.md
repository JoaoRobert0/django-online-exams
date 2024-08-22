# Documento de Visão

## Histórico de Revisões

| Data                |  Versão             |          Descrição  |  Autores            |
| :------------------ | :------------------ | :------------------ | :------------------ |
| 22/08/2024 | 1.0 | Versão inicial | João Roberto |


## 1. Objetivo do projeto

O objetivo principal deste sistema é fornecer uma plataforma robusta para o gerenciamento e resposta a simulados online. O sistema permitirá que usuários autenticados cadastram questões objetivas, incluindo enunciado, alternativas e a resposta correta. Após o cadastramento de um conjunto de questões, o sistema possibilitará a criação de simulados que podem ser configurados com diferentes questões e pesos atribuídos a elas. Esses simulados estarão disponíveis para serem respondidos pelo público geral, facilitando a prática e avaliação de conhecimentos de forma eficiente e acessível.

## 2. Descrição do problema
| | |
| - | - |
| **Problema** | A falta de uma plataforma centralizada para a criação e administração de simulados online dificulta o processo de cadastramento e gerenciamento de questões e simulados, além de limitar a acessibilidade e a prática de conhecimentos para o público geral. |
| **Afeta**    | Estudantes, educadores e qualquer pessoa que deseje criar, gerenciar e participar de simulados online para fins de avaliação e aprendizado. |  
| **Impacta**  | A ausência de uma solução integrada pode levar a uma gestão ineficiente dos simulados, dificultando o acompanhamento e a prática de testes, além de reduzir a eficácia das avaliações educacionais. |
| **Solução**  | Desenvolver um sistema que permita aos usuários autenticados cadastrar questões objetivas, criar simulados com questões e pesos personalizados e disponibilizar esses simulados para o público geral responder, promovendo uma prática mais acessível e organizada. | 

## 3. Descrição dos usuários 

| Nome | Descrição | Responsabilidade |
| :-: | - | - |
| **Visitante** | Usuário não autenticado que acessa o sistema para responder simulados disponíveis publicamente. | - Responder aos simulados disponíveis.<br>- Visualizar o progresso e resultados dos simulados. |
| **Moderador** | Usuário autenticado com permissões administrativas e de gerenciamento de conteúdo. | - Cadastrar e gerenciar questões objetivas.<br>- Criar e configurar simulados com questões e pesos.<br>- Monitorar e gerenciar o conteúdo dos simulados.<br>- Acompanhar e avaliar o uso e o desempenho dos simulados. |

## 4. Descrição do ambiente dos usuários

| Nome | Descrição |
| :-: | :--
| **Visitante** | O visitante acessa o sistema através de um navegador web moderno (como Chrome, Firefox, Safari) em qualquer dispositivo (computador, tablet ou smartphone). Não é necessário login para responder aos simulados, mas o visitante precisa estar conectado à internet para acessar e interagir com o conteúdo dos simulados disponíveis publicamente. O visitante tem acesso limitado às funcionalidades do sistema, podendo apenas responder a simulados e visualizar seus resultados. |
| **Moderador** | O moderador utiliza um navegador web moderno (como Chrome, Firefox, Safari) em um computador, tablet ou smartphone com conexão à internet para acessar a plataforma. Para a melhor experiência e funcionalidades completas, é recomendado o uso de um computador desktop ou laptop. O moderador tem acesso a áreas administrativas e ferramentas de gerenciamento do sistema, como cadastro e edição de questões, configuração de simulados e análise de dados de uso e desempenho. |

## 5. Principais necessidades dos usuários

| Nome | Necessidade |
| :-: | :--
| **Visitante** |  - **Acesso fácil e rápido a simulados:** O visitante precisa poder acessar e responder aos simulados de maneira intuitiva e sem necessidade de autenticação.<br> - **Resultados e feedback:** O visitante necessita visualizar o progresso e os resultados dos simulados de forma clara e detalhada para avaliar seu desempenho.<br>- **Interface responsiva:** O sistema deve ser compatível com diferentes dispositivos e tamanhos de tela para garantir uma experiência de usuário consistente. |
|  **Moderador** | - **Cadastro e gerenciamento de questões:** O moderador precisa de uma interface eficiente para cadastrar, editar e remover questões objetivas.<br>- **Criação e configuração de simulados:** O moderador deve ser capaz de criar simulados com diferentes questões, pesos e configurações, facilitando a personalização dos testes.<br>- **Monitoramento e análise:** O moderador necessita de ferramentas para acompanhar o uso dos simulados e analisar o desempenho dos participantes, incluindo relatórios e estatísticas detalhadas. |

## 6. Alternativas concorrentes

| Nome da Alternativa | **Pontos fortes** | **Pontos fracos** | **Semelhanças com o nosso projeto** | **Diferenciação do nosso projeto em relação aos similares** |
|---------------------|--------------------|--------------------|------------------------------------|------------------------------------------------------------|
| **Quizlet**         | - Interface amigável e fácil de usar.<br>- Ampla base de dados de questões e flashcards.<br>- Funcionalidades de estudo e revisão. | - Limitações na personalização de simulados.<br>- Dependência de uma base de dados preexistente.<br>- Recursos avançados podem requerer uma assinatura paga. | - Permite criação e resposta a quizzes.<br>- Acesso a uma ampla gama de questões e tópicos. | - Foco na personalização avançada de simulados.<br>- Possibilidade de criar simulados com pesos personalizados para questões.<br>- Integração de ferramentas de monitoramento e análise detalhada. |
| **Kahoot!**         | - Engajamento alto com uma interface de jogo.<br>- Facilita a criação rápida de quizzes.<br>- Uso popular em ambientes educacionais. | - Foco em jogos e quizzes rápidos, com menos recursos para simulados aprofundados.<br>- Funcionalidades limitadas para configuração avançada de simulados. | - Permite criação de quizzes e participação em tempo real.<br>- Acesso a uma comunidade de usuários e quizzes compartilhados. | - Oferece opções avançadas de configuração e personalização.<br>- Mais voltado para avaliação profunda e análise detalhada de desempenho. |
| **Google Forms**    | - Flexibilidade para criar vários tipos de formulários e questionários.<br>- Integração com outras ferramentas Google.<br>- Gratuito e acessível. | - Menos foco em simulados específicos.<br>- Recursos limitados para análise avançada e personalização de simulados.<br>- Interface menos focada em experiência de aprendizado. | - Criação e compartilhamento de questionários.<br>- Possibilidade de responder aos questionários online. | - Foco exclusivo em simulados com opções avançadas de personalização e análise.<br>- Interface projetada especificamente para a criação e gestão de simulados e questões objetivas. |
| **ProProfs Quiz Maker** | - Ferramentas de criação de quizzes e simulados bastante robustas.<br>- Recursos para análise e relatórios detalhados.<br>- Opções de personalização e branding. | - Versão gratuita com funcionalidades limitadas.<br>- Interface pode ser complexa para novos usuários.<br>- Recursos avançados estão disponíveis apenas em planos pagos. | - Criação e configuração de simulados com relatórios detalhados.<br>- Opções de personalização. | - Mais acessível com funcionalidades avançadas de forma gratuita.<br>- Foco em uma interface intuitiva e fácil de usar.<br>- Integração de ferramentas de análise com acesso gratuito. |

## 7. Visão geral do produto

O sistema será uma plataforma online destinada ao gerenciamento e resposta a simulados. Com foco em uma experiência de usuário intuitiva, o sistema permitirá que usuários autenticados criem e gerenciem questões objetivas e simulados, enquanto os visitantes poderão acessar e responder aos simulados disponibilizados publicamente. O sistema oferecerá funcionalidades para personalização de simulados, incluindo a atribuição de pesos às questões, e fornecerá ferramentas de análise para monitorar o desempenho dos usuários e a eficácia dos simulados. A interface será responsiva e acessível de diferentes dispositivos, garantindo uma experiência consistente e eficiente para todos os usuários.

## 8. Requisitos funcionais

| Código | Nome                       | Descrição                                                                                       | Prioridade |
|--------|----------------------------|-------------------------------------------------------------------------------------------------|------------|
| RF001  | Cadastro de questões        | Permitir que o moderador cadastre novas questões objetivas, incluindo enunciado, alternativas e resposta correta. | **Alta**       |
| RF002  | Criação de simulados        | Permitir que o moderador crie simulados configurando questões e pesos associados a cada uma.     | **Alta**      |
| RF003  | Resolução de simulados      | Permitir que o visitante responda aos simulados disponíveis publicamente e visualize seus resultados. | **Alta**     |
| RF004  | Análise de desempenho       | Fornecer ao moderador ferramentas para monitorar e analisar o desempenho dos participantes nos simulados. | **Média**   |
| RF005  | Interface responsiva        | Garantir que a interface do sistema seja acessível e funcional em diferentes dispositivos e tamanhos de tela. | **Alta**   |

## 9. Requisitos não-funcionais

| Código              | Nome                   | Descrição                                                                                           | Categoria           | Classificação |
|---------------------|------------------------|-----------------------------------------------------------------------------------------------------|----------------------|---------------|
| RNF001              | Desempenho             | O sistema deve suportar um número elevado de usuários simultâneos sem comprometer o desempenho.    | Desempenho           | **Alta**          |
| RNF002              | Segurança              | Dados dos usuários e simulados devem ser protegidos contra acesso não autorizado e vazamentos.    | Segurança            | **Alta**          |
| RNF003              | Usabilidade            | O sistema deve ter uma interface intuitiva e fácil de usar para todos os tipos de usuários.         | Usabilidade          | **Alta**          |
| RNF004              | Manutenibilidade       | O sistema deve ser fácil de atualizar e manter, com documentação adequada para desenvolvedores.     | Manutenção           | **Média**         |
| RNF005              | Compatibilidade        | O sistema deve ser compatível com os principais navegadores web e dispositivos móveis.              | Compatibilidade      | **Alta**          |
