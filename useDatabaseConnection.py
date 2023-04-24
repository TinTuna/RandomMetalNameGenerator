import pymysql
import useEnvVars

# database connection
connection = pymysql.connect(host="193.31.31.132", port=3306, user=useEnvVars.MM_DATABASE_USER, passwd=useEnvVars.MM_DATABASE_PWD, database="s91300_MetalMonthly")
cursor = connection.cursor()
print("Connection successful", connection)
# some other statements  with the help of cursor
connection.close()