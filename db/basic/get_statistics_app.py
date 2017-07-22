#-*- coding:utf-8
import MySQLdb
def count_developer_app(output_path):
    db = MySQLdb.connect(host="127.0.0.1", user="root",
                         passwd="123456", db="app_info")
    cursor = db.cursor()
    results = "app_number    developer_number\n"
    for i in range(1,):
        cursor.execute("SELECT count(DISTINCT developer_name) FROM app_detail GROUP BY developer_name HAVING COUNT(*)=" + str(i))
        count = cursor.fetchone()
        if(count == None):
            continue
        print str(i) + '\t' + count[0] + '\n'
        results = results + str(i) + '\t' + count[0] + '\n'
    outfile = open(output_path, "w")
    outfile.write(results)
    outfile.close()


##test .
print "start"
count_developer_app("../results/count_developer_app")
print "end"