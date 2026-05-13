# Escolha do modelo:

#### A escolha do modelo foi baseada principalmente nos custos das IAS e nos benchmarks: OCRBench, MathVista e AI2D.

#### - Comparados o custo benefícios das IAs, foram selecionados 4 modelos: GPT-4.1-mini, GPT-5-nano, GPT-5-mini e GPT-4o-mini.

|              |           |          |       |             |             |              |
| ------------ | --------- | -------- | ----- | ----------- | ----------- | ------------ |
| Modelo       | MathVista | OCRBench | AI2D  | Input (US$) | Cache (US$) | Output (US$) |
| GPT-4.1-mini | 70.90     | 840      | 76.00 | 0,4         | 0,04        | 1,6          |
| GPT-5-nano   | 73.10     | 747      | 81.40 | 0,05        | 0,005       | 0,4          |
| GPT-5-mini   | 79.2      | 828      | 86.7  | 0.25        | 0.03        | 2.00         |
| GPT-4o-mini  | 52.50     | 785      | 77.80 | 0,15        | 0,075       | 0,6          |

*Modelos / Pontuações / Custos per M/tokens*

###### Focos dos benchmarks:

+ CRBench - Capacidade de reconhecimento ótico de caracteres (OCR) e compreensão de documentos.

+ MathVista - Cálculos matemáticas e leitura e interpretação de gráficos

+ AI2D - Resolução de questões de múltipla escolha que exigem que o modelo faça o mapeamento e a correlação entre os elementos visuais (setas, nós, estruturas), a iconografia e os rótulos textuais inseridos no diagrama para inferir processos científicos.

###### Realização de testes e escolha definitiva dos modelos.

+ Primeiramente foram análisados os resultados da respostas, e confirmando os resultados do benchmark OCRBench de reconhecimento e compreensão de documentos: tivemos respostas mais concisas utilizando o modelo 4.1-mini e 5-mini e mais alucinações com os modelos 5-nano e 4o-mini. A interpretação de gráficos e correlacionamento de dados foi semelhante para os modelos 4.1-mini. 5-mini e 5-nano, mas com algumas alucinações do modelo 5-nano em alguns testes. O modelo ***5-mini foi o que teve melhor desempenho*** e 4o-mini o pior.

+ Teste de gastos:

pergunta:

"Sabendo que o Fator de Utilização Total (FUT) do parque de refino atingiu 95% , como a sazonalidade do mercado interno e as ações de terceiros explicam matematicamente e operacionalmente a queda expressiva de 67,3% nas importações de diesel entre o 4T25 e o 1T26?" + pdf.

gpt-4.1-mini:

+ "input_tokens": 14416 

+ "output_tokens": 698 

+ "total_tokens": 15114 

+  (14416 * 0,4)/10^6 + (698 * 1,6)/10^6 = $0.0068 por uso.

gpt-5-nano:

+ "completion_tokens": 6990

+ "prompt_tokens": 14414

+ "total_tokens": 21404

+ (14414 * 0,05)/10^6 + (6990 *0,6)/10^6 = 0.0049 por uso

gpt-5-mini:

+ "completion_tokens": 2573

+ "prompt_tokens": 14414

+ "total_tokens": 16987

    (14414 * 0,25)/10^6 + (2573*2)/10^6 = $0.0087 por uso

Dada as comparações. optei por escolher o gpt-4.1-mini, pois foi muito superior ao gpt-5-nano nos testes e conseguiu ter um desempenho semelhante ao gpt-5-mini tendo um custo 20% menor.



# Uso do script
