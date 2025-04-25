from crewai import Agent, Task, Crew, LLM, Process


# Definir modelo #
deepseek_llm = LLM(
  model="ollama/deepseek-r1:8b",
  temperature=0.1,
  base_url="http://localhost:11434"
)

# Um agente para ser o marcelo #
marcelo_agente = Agent(
    role = """
    Profissional de sistemas de informação graduado com atuação 
    em desenvolvimento com django e engenharia de dados e análise 
    de dados.
    """,
    goal = """
    Responder detalhadamende suas experiências
    """,
    backstory = """
    Trabalhei na empresa Ideyas inovation usando framework Django 
    da linguagem de programação Python, para construção de um 
    sistema de Trade Bulking,no periodo de Fevereiro de 
    2020 até Janeiro de 2021.
    """,
    llm=deepseek_llm
)

# Um agente para ser o revisor
marcelo_revisor = Agent(
  role = """
  Revisor de experiências profissionais 
  """,
  goal= """
  Revisar e corrigir informações de experiencia profissional  
  """,
  backstory= """
  Você é um agente especialista em reponder perguntas para recrutadores
  utlizando palvras chaves.
  """,
  llm = deepseek_llm
)

# task tarefa a ser executada
tarefa_marcelo = Task(
  description = """
  Conte um pouco sobre sua experiência em python
  """,
  expected_output = """
  Um texto de até 2000 caracteres expliacno de maneira detalhada suas experiência 
  """,
  agent = marcelo_agente
)


# Crew Flow
crew = Crew(
  agents = [marcelo_agente],
  tasks = [tarefa_marcelo],
  process = Process.sequential,
  verbose = True
)
crew.kickoff()