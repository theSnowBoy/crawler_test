#-*- coding:utf-8
import MySQLdb
def get_data_from_db(sql):
    # 打开数据库连接
    db = MySQLdb.connect(host="127.0.0.1", user="root",
                            passwd="123456", db="app_info")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute(sql)
    cursor.execute()

    # 使用 fetchone() 方法获取一条数据库。
    datas = cursor.fetchall()
    texts = [ data[0] for data in datas ]
    # 关闭数据库连接
    cursor.close()
    db.close()
    return texts

class DBHelper:
    def __init__(self, host="127.0.0.1", user="root",
                 passwd="123456", db="app_info"):
        self.db = MySQLdb.connect(host,user,passwd,db)
        self.cursor = self.db.cursor()
        print "connected :" + db

    def insert_app_info(self,sql,data_set):
        print sql
        cursor = self.db.cursor()
        cursor.executemany(sql, data_set)
        self.db.commit()
        cursor.close()
        print "inserted"


    def insert_app_topics(self,apps):
        print "inserting app topics"
        sql = "INSERT IGNORE INTO topic_app(docid,version_code,developer_name,num_downloads,topic_id,probability) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor = self.db.cursor()
        cursor.executemany(sql,apps)
        self.db.commit()
        cursor.close()
        print "app topics inserted"

    def insert_topic_envs(self,topic_envs):
        print "inserting topics envs ..."
        sql = "INSERT IGNORE INTO topic_info_environment(topic_id,popularity,products,mean_popularity,standard_deviation) VALUES(%s,%s,%s,%s,%s)"
        cursor = self.db.cursor()
        cursor.executemany(sql, topic_envs)
        self.db.commit()
        cursor.close()
        print "environment inserted "


    def get_apps(self,table_name = "app_shopping2"):
        print "get app info from : " + table_name
        sql = "SELECT docid,version_code,developer_name,num_downloads,description_html,ratings_count FROM " + table_name  # + " limit 10" #test
        cursor = self.db.cursor()
        cursor.execute(sql)
        apps = cursor.fetchall() # 注意大数据量情况。
        return apps

    '''
    用于构建环境（需求，竞争）
    '''
    def get_topic_info(self,topic_id):
        sql = "select num_downloads,probability from topic_app where topic_id = "+ topic_id
        cursor = self.db.cursor()
        cursor.execute(sql)
        topic_info = cursor.fetchall() # 二元组（num_downloads，probability）列表
        cursor.close()
        return topic_info

    '''
    度量 用户实力
    '''
    def get_developer_info(self,developer_name):
        sql = "select topic_id,num_downloads,probability from topic_app where developer = "+ developer_name
        cursor = self.db.cursor()
        cursor.execute(sql)
        developer_info = cursor.fetchall()  # 三元组（topic_id,num_downloads,probability）列表
        cursor.close()
        return developer_info

    def get_app_info(self,sql):
        # cursor = self.db.cursor()
        self.cursor.execute(sql)
        app_info = self.cursor.fetchall()
        return app_info

    def close(self):
        self.cursor.close()
        self.db.close()

