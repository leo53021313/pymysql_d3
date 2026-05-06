# 引入所需套件
import pymysql
from configparser import ConfigParser


# 讀取 config.ini 檔案取得資料庫連線資訊
config = ConfigParser()
config.read('config.ini')
    
class SqlManager:
    dbs = "SHOW DATABASES;"
    full_passengers = "select * from my_titanic.full_passengers;"


    def __init__(self):
        self.connection = pymysql.connect(
            host=config.get('DB', 'host'),
            user=config.get('DB', 'user'),
            password=config.get('DB', 'password'),
            port=config.getint('DB', 'port'),
            cursorclass=pymysql.cursors.DictCursor
        )

    def sql_query(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
        return result
    
    def get_leonard_males(self):
        result = self.sql_query(self.full_passengers)

        leonard_male = []
        for r in result:
            if "Leonard" in r['pname'] and r['sex'] == 'male' and r['pname'].startswith('Leonard') is False:
                leonard_male.append({
                    'id': r['id'],
                    'pclass': r['pclass'],
                    'pname': r['pname']
                })
        
        return leonard_male


# 建立 function 執行 SQL 查詢
