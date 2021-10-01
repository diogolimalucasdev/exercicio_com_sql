<h1>Exercicio_com_sql </h1>

<h3> Apos iniciado a pasta que eu criei com Nome de "exercicio_com_sql" no Pycharm, crio um arquivo chamado models.py
    <p>
    Nesse arquivo vao conter as classes que vao referenciar as tabelas do banco de dados
    </p>
</h3>


<h3> No terminal digito pip install sqlalchemy </h3>
  
 ````Windows PowerShell
      pip install sqlalchemy
  ````
<h2>Agora precisamos fazer os imports...</h2>

````Python
      from sqlalchemy import create_engine
  ````

<h2>Criando o banco... </h2>
<h3>  <strong> engine = create_engine('sqlite:///nomedobanco') </strong>
no meu caso ficou assim... </h3>


```Python
engine = create_engine('sqlite:///Exercicio.db',convert_unicode=True)

```
**convert_unicode = True é para nao ter problemas com acentuações no banco de dados**

<h2> -Criando a sessao do banco de dados, fazemos mais uma importação e adicionamos uma linha de codigo, o autocommit=False é para nao commit sozinho e o bind=engine é um parametro para ele saber qual banco ele vai abrir a sessao</h2>

  ```Python


from sqlalchemy.orm import scoped_session, sessionmaker

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))
```
**O engine é como o SQLAlchemy se comunica com o banco de dados. Portanto, ao criar o mecanismo, você deve adicionar a URL do banco de dados (chamada pela abreviação em inglês db) e é basicamente isso.**

<h2>Fazemos o import da declaritive base que é um default do sqlalchemy e adicionamos um trecho para se criar o banco e para pode fazer consultas no banco com query </h2>


  ```Python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.query = db_session.query_property()


```

<h2>Agora criamos a tabela por meio da classe: *o nome da tabela nao é o nome da classe mas por boas praticas eu sigo o mesmo nome.Fazemos mais uma importação dentro do sqlalchemy
**Importei o Column, Integer, String**. Column é para eu poder criar uma coluna, Integer é pra poder adicionar tipo inteiro e String para adicionar texto </h2>

  ```Python
from sqlalchemy import create_engine, Column, Integer, String

class Programador(Base):
    __tablenamee__ = 'programador'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80), index=True)
    idade = Column(Integer)
    email = Column(String(80), index=True)
    
    
class Habilidades(Base):
    __tablename__ = 'habilidade'
    id = Column(Integer, primary_key=True)
    habilidade = Column(String(40))

```

<h2> trabalhando com ForeignKey e o relationship </h2>
    <h3>O foreignKey é uma chave estrangeira onde  eu relaciono uma tabela com a outra assim.... </h3>
    
 ```Python
   class Programador_Habilidade2(Base):
    __tablename__ = 'programador_habilidades'
    id = Column(Integer, primary_key=True)
    programador_id = Column(Integer, ForeignKey('programador.id'))
    programador_habilidade = Column(String(80), ForeignKey('habilidade.habilidade'))
    programador = relationship("Programador")
    habilidade = relationship("Habilidade")
    		
```
  <h3> 	O ForeignKey me permite buscar em outra tabela um dado e o   relationship reconhece que tem uma relação de uma tabela com a outra </h3>

<h2> 
Agora crio uma função chamada init_db(),onde eu coloco o comando que ira criar meu banco de dados </h2>

```Python

    def init_db():
    Base.metadata.create_all(bind=engine)
    
    
if __name__ == '__main__':
    init_db()
    
````






    
