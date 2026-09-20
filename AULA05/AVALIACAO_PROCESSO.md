Cenário:

1. Nome do Processo
2. É viável para RPA? (Sim / Não)
3. Justificativa baseada nos 4 critérios essenciais (Repetitividade, Regras de Negócio, Tipo de Dados, Volume).
4. Mapeamento Passo a Passo das Ações do Robô


1=Conciliação bancária diária feita a partir do download do extrato `.csv` e comparação das linhas com as baixas do sistema ERP via regras fixas de CNPJ e valor.

2= Sim.

3=  REPETITIVIDADE:
Baixar o CSV e comparar os dados e informações com o sistema de registro do ERP da Empresa. Assim vendo se nao tem nenhuma diferença entre elas.

    REGRAS DE NERGOCIO:
Os dados bancarios de informações da Empresa tem que estar de acordo com o ERP e CSV. Os dois tem que ter as mesmas informções.

-Mesmo CNPJ
-Mesmo valor
-Mesma data
-Mesma operação

    TIPO DE DADOS:
Os arquivos do CSV e ERP, tem dados com organização padronizada em colunas.

 VOLUMES:
O processo envolve muitas transações por dia e pagamentos e muitas movimentações para conferencia dos arquivos e dados.

4= Mapeamento Passo a Passo das Ações do Robô:


1- Bixar documento CSV do dia;

2- Abrir o ERP;

3- Buscar as Baixas do mesmo periodo, fazendo um filtro do dia;

4- O Bot ira acessar e ler o arquivo CSV do dia atual, indentificar as colunas CNPJ, e analisar data, valor, etc... e depois acessar o ERP e buscar as baixas do mesmo periodo e dia. Filtro;

5- Ler cada linha do CSV junto com as baixas do ERP usando o CNPJ, valor, data e as outras informações de dados;

6- Ira processar a leitura e processar se o CNPJ, valor, data etc... estao de acordo. Se houver aguma diferença nos dados ira avisar no sistema como "Informções do documento do ERP incorretos" e depois continuar o processo. Assim analisando e vizualizando outros documentos do mesmo dia e horario. Os arquivos que estiverem com dados e informações incorretos ou alguma diferença, iram ser classificados como "Arquivo ERP incorreto" marcado em vermelho;

7- Se estiver tudo em horden e as informções dos dois documentos do dia nao tiverem com alguma diferença, ira avisar no sistema como "Arquivos de transição corretos" e ira registrar no sistema o documento, classificando como "Analise de conferencia OK" marcado em verde.

8- O Bot continua esse processo até que todos os arquivos do CSV e ERP estejam conferidos.