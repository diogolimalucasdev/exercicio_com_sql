from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

engine = create_engine('sqlite:///exercicio.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Programador(Base):
    __tablename__ = 'programador'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80), index=True)
    idade = Column(Integer)
    email = Column(String(80))

    def __repr__(self):
        return f"pessoa{self.nome}"


class Habilidades(Base):
    __tablename__ = 'habilidade'
    id = Column(Integer, primary_key=True)
    habilidade = Column(String(40))


class Programador_Habilidade2(Base):
    __tablename__ = 'programador_habilidades'
    id = Column(Integer, primary_key=True)
    programador_id = Column(Integer, ForeignKey('programador.id'))
    programador_habilidade = Column(String(80), ForeignKey('habilidade.habilidade'))
    programador = relationship("Programador")
    habilidade = relationship("Habilidade")


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
