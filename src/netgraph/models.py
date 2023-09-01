from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

# Определение модели класса Node
class Node(Base):
    __tablename__ = 'node'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String, nullable=False)
    name = Column(String, nullable=True)
    hostname = Column(String, nullable=True)
    model = Column(String, nullable=False, default="unknown")
    mac = Column(String, nullable=True)
    uplink = Column(Integer, nullable=True)
    ro_community = Column(String, nullable=True, default="private_otu")
    rw_community = Column(String, nullable=True)
    level = Column(Integer, nullable=False, default=1)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    netmap_id = Column(Integer, ForeignKey('netmap.id'))

# Определение модели класса Edge
class Edge(Base):
    __tablename__ = 'edge'
    id = Column(Integer, primary_key=True, autoincrement=True)
    source_id = Column(Integer, ForeignKey('node.id'))
    source_port = Column(Integer, nullable=False)
    target_id = Column(Integer, ForeignKey('node.id'))
    target_port = Column(Integer, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    netmap_id = Column(Integer, ForeignKey('netmap.id'))

# Определение модели класса Netmap
class Netmap(Base):
    __tablename__ = 'netmap'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String,nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    nodes = relationship('Node', backref='netmap', lazy=True)  # Отношение один-ко-многим с Node
    edges = relationship('Edge', backref='netmap', lazy=True)  # Отношение один-ко-многим с Edge
    