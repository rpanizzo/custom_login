from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (scoped_session,sessionmaker,)
from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
)
import bcrypt

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)

    def check_password(self, password):
        expected_hash = self.password.encode('utf8')
        return bcrypt.checkpw(password.encode('utf8'), expected_hash)

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')
