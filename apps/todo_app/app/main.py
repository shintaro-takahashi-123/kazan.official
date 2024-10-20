# FastAPIアプリケーションのメインファイル

from fastapi import FastAPI
from sqlalchemy import create_engine # データベースとの接続をする「エンジン」を作る関数
from sqlalchemy.ext.declarative import declarative_base # DBのテーブルを定義市（SQLAlchemyのベースクラスを作成）
from sqlalchemy.orm import sessionmaker # DBとのセッションを作る関数


# ここに、指定のデータベースのユザネ、パスワードを指定する
DATABASE_URL = "postgresql://maeda:maedanobu723@localhost/todo_app"

# エンジンの宣言
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
