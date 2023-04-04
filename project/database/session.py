from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # 호출되었을 때 세션 생성

Base = declarative_base()   # 베이스 모델이며 상속되어 DB 모델 클래스들과 연결됨. 테이블명이 일치하는 모델을 찾아 쿼리문을 실행.