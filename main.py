import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
#carregar chave api
load_dotenv()
apikey = os.getenv("OPENAI_API_KEY")

inputUsuario = input("faça uma pergunta:")
#carregar arquivo
file_path = "pdfs/arquivo.pdf"
loader = PyMuPDFLoader(file_path)
pages = loader.load()

texto_pdf = "\n".join([page.page_content for page in pages])
#modelo
model = ChatOpenAI(model="gpt-4o-mini",
                   api_key=apikey,
                   temperature=0)


prompt = ChatPromptTemplate.from_messages([
    ("system", """você é um analista, irá verificar os pontos do pdf e trazer os dados nos formatos:"
    • O campo text deve conter Markdown válido com títulos, listas e destaques
• O campo source deve identificar o nome ou título do documento analisado
• O campo suggestions deve ter exatamente 3 perguntas de acompanhamento
relevantes
• A resposta final deve ser um JSON válido e parseável — sem texto fora do objeto"""),
("user", "Documento:\n{contexto}\n\nComando: {comando}")
])

chain = prompt | model
resposta = chain.invoke({"contexto": texto_pdf,
                         "comando": inputUsuario})

print(resposta.content)

