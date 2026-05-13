import os
import pdfplumber
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
#from langchain_core.globals import set_debug
#set_debug(True)

load_dotenv()

class OutputFormat(BaseModel):
    type: str = Field(default="text", description="Sempre deve ter o valor 'text'")
    text: str = Field(description="Sua resposta contendo o conteúdo em Markdown válido")
    source: str = Field(description="Identificar o nome ou título do documento")
    suggestions: list[str] = Field(description="Exatamente 3 perguntas de acompanhamento relevantes")

def parse_pdf_to_markdown_local(file_path):
    conteudo_completo = []
    
    with pdfplumber.open(file_path) as pdf:
        for num_pagina, pagina in enumerate(pdf.pages):
       
            texto = pagina.extract_text()
            if texto:
                conteudo_completo.append(f"## Página {num_pagina + 1}\n{texto}\n")
            
            tabelas = pagina.extract_tables()
            for tabela in tabelas:
                conteudo_completo.append("\n### Tabela Extraída:")
                for index, linha in enumerate(tabela):
                   
                    linha_limpa = [str(celula).replace('\n', ' ').strip() if celula else " " for celula in linha]
                    linha_md = "| " + " | ".join(linha_limpa) + " |"
                    conteudo_completo.append(linha_md)
                    
                 
                    if index == 0:
                        divisor = "| " + " | ".join(["---"] * len(linha_limpa)) + " |"
                        conteudo_completo.append(divisor)
                conteudo_completo.append("\n")

    return "\n".join(conteudo_completo)

print("Extraindo e formatando PDF localmente...")
file_path = "pdfs/petrobras.pdf"
texto_estruturado = parse_pdf_to_markdown_local(file_path)


model = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
structured_model = model.with_structured_output(OutputFormat)

prompt = ChatPromptTemplate.from_messages([
    ("system", """Você é um analista. 
    O documento fornecido foi extraído com tabelas em formato Markdown. 
    Cruze os dados corretamente, respeitando linhas e colunas."""),
    ("user", "Documento:\n{contexto}\n\nComando: {comando}")
])

chain = prompt | structured_model

inputUsuario = input("Faça uma pergunta: ")

resposta = chain.invoke({
    "contexto": texto_estruturado,
    "comando": inputUsuario
})

print(resposta.model_dump_json(indent=2))