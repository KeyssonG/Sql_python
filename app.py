import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-B107SNR;"
    "Database=SUCOS_VENDAS;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida")

cursor = conexao.cursor()



comando = """

    CREATE TABLE [TABELA DE CLIENTES](
    
    [CPF] [CHAR] (11),
    [NOME] [VARCHAR] (150),
    [RUA] [VARCHAR] (150),
    [COMPLEMENTO] [VARCHAR] (150),
    [BAIRRO] [VARCHAR] (150),
    [ESTADO] [CHAR] (2),
    [CEP] [CHAR] (8),
    [DATA DE NASCIMENTO] [DATE],
    [IDADE] [SMALLINT],
    [SEXO] [CHAR] (1),
    [LIMITE DE CREDITO] [MONEY],
    [VOLUME MINIMO] [FLOAT],
    [PRIMEIRA COMPRA] [BIT] 

    )

"""

cursor.execute(comando)
cursor.commit()