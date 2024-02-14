from dotenv import load_dotenv
import os
     
load_dotenv()


def get_connection():
    try:
        host = os.environ["MYSQL_HOST"]
        user = os.environ["MYSQL_USER"]
        password = os.environ["MYSQL_PASSWORD"]
        db = os.environ["MYSQL_DATABASE"]
        DATABASE_CONECTION_URI = f"mysql+pymysql://{user}:{password}@{host}/{db}"
        return DATABASE_CONECTION_URI

    except Exception as ec:
        print(ec)