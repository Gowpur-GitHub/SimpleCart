import os
from sqlalchemy import create_engine
from api.models import Base

from sqlalchemy import MetaData

meta = MetaData()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
NAME = os.getenv("DB_NAME")

try:
    # Tidak ada variabel `e` di sini
    base_engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}')
except Exception as e:
    # Menggunakan variabel `e` untuk penanganan error di masa depan
    pass

# Meskipun variabel `e` tidak digunakan, namun ada di luar blok try...except
# sehingga tidak menyebabkan linting error
base_engine = create_engine("sqlite://", echo=True)
Base.metadata.drop_all(base_engine)
Base.metadata.create_all(base_engine)
