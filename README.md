# Lauan Gabriell

**Estudante de Inteligência Artificial · Python, machine learning e desenvolvimento web**

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/branding/studio.png">
  <img src="./assets/pixel-character/animations/studio.gif" width="768" alt="Estúdio em pixel art ao anoitecer. Lauan caminha pelo cômodo, usa o celular, programa no notebook e acena.">
</picture>

[Projetos](#projetos) · [Tecnologias](#tecnologias) · [Contato](#contato) · [Ilustração estática](./assets/branding/studio.png)

## Sobre mim

Estudo Inteligência Artificial no Piauí Instituto de Tecnologia (PIT). Gosto de acompanhar um projeto do primeiro desenho da interface até a API, o banco de dados e a avaliação do modelo. Em AI Engineering, me interessa especialmente como um sistema lida com dados incompletos e permite que a pessoa corrija o que a IA interpretou.

## Projetos

### VETOR · Agente de previsão de entregas

<img src="./assets/projects/vetor.svg" width="768" alt="">

No VETOR, desenvolvo o **Deiv**, um agente que transforma uma conversa em português em dados para estimar o tempo de uma entrega. O agente interpreta a mensagem com Qwen2 via Ollama, valida os campos e aguarda a confirmação antes de chamar o serviço de inferência.

**Destaque técnico** · Duas APIs FastAPI separam o diálogo da inferência com Random Forest. O projeto é experimental e a execução completa exige um artefato de modelo compatível.

**Tecnologias** · Python, FastAPI, scikit-learn, Ollama, React e TypeScript

[Abrir repositório](https://github.com/lauangabriell/Delivery-Intelligence-Agent) · [Ver arquitetura](https://github.com/lauangabriell/Delivery-Intelligence-Agent/blob/main/docs/ARCHITECTURE.md)

### DIKE · Plataforma de estudos jurídicos

<img src="./assets/projects/dike.svg" width="768" alt="">

Sou cofundador da DIKE e desenvolvo toda a parte técnica da plataforma, do frontend ao backend, banco de dados e integrações de IA. A plataforma reúne questões e flashcards para quem estuda Direito, OAB e concursos.

**Destaque técnico** · Passei os filtros e a paginação do banco de questões para o PostgreSQL, de modo que cada consulta devolva só a página solicitada.

**Tecnologias** · JavaScript, Supabase, PostgreSQL e API Gemini

[Conhecer a plataforma](https://dike-estudos-juridicos.pages.dev/)

### Observatório de Reputação · Análise de sentimentos

<img src="./assets/projects/observatorio.svg" width="768" alt="">

Montei um pipeline que coleta comentários do YouTube, classifica o sentimento e permite explorar as previsões em um painel Streamlit. Usei comentários sobre o Nubank como recorte inicial do projeto acadêmico.

**Destaque técnico** · Comparei TF-IDF e embeddings com regressão logística e acompanhei o recall por classe. Em um dos experimentos, a acurácia subiu enquanto o recall dos comentários positivos caiu.

**Tecnologias** · Python, YouTube Data API, pandas, scikit-learn e Streamlit

[Abrir repositório e experimentos](https://github.com/lauangabriell/observatorio-reputacao)

### TEIA · Assistente de adaptação pedagógica

<img src="./assets/projects/teia.svg" width="768" alt="">

Idealizei a TEIA e participei da liderança e do desenvolvimento do MVP. Trabalhei nos prompts e na integração com Gemini para apoiar professores na adaptação de atividades para estudantes com TEA, preservando o objetivo pedagógico do material.

**Destaque técnico** · O assistente recebe a atividade original e o perfil de aprendizagem informado pelo professor para propor uma versão adaptada.

**Tecnologias** · Node.js, Express, Gemini, HTML, CSS e JavaScript

[Abrir repositório](https://github.com/lauangabriell/TEIA-MVPv1) · [Ver MVP](https://teia-henna.vercel.app/)

## Tecnologias

- **IA e machine learning** · scikit-learn, pandas, TF-IDF, regressão logística, Random Forest, Gemini e Ollama
- **Backend e APIs** · Python, FastAPI, Node.js e Express
- **Dados** · SQL, PostgreSQL e Supabase
- **Frontend** · HTML, CSS, JavaScript, React, TypeScript e Streamlit
- **Ferramentas e infraestrutura** · Git, GitHub, Vite, Cloudflare Pages e Vercel

## Em desenvolvimento

No Deiv, estou explorando como reaproveitar os dados autorizados do turno e revisar cada entrega em uma única confirmação. No Observatório, aprofundo a avaliação por classe e a identificação de comentários que precisam de revisão humana.

## Trajetória

Na TEIA, comecei a ligar interfaces web a modelos por API. A DIKE ampliou esse trabalho para o banco de dados e a manutenção de um produto. Com o Observatório e o VETOR, passei a treinar modelos, comparar resultados e integrar previsões a aplicações que outras pessoas podem usar.

## Contato

[LinkedIn](https://www.linkedin.com/in/lauan-gabriell-91741b38a/) · [GitHub](https://github.com/lauangabriell)

<img src="./assets/pixel-character/sprites/wave.png" width="62" alt="Lauan em pixel art acena na despedida.">
