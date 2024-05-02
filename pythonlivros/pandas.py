import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import sqlite3
conexao = mysql.connector.connect(
    user = 'root',
    password = 'root',
    database = 'meus_livros'
)

engine = sqlite3.connect('sqlite:meus_livros.db')


df = pd.read_sql_query('SELECT * FROM proximos_livros',engine)

print(df.head())

