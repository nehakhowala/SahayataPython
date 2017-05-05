import MySQLdb
from flask import jsonify

conn = MySQLdb.connect(host="sahayata1.cq3lebnygdgj.us-west-1.rds.amazonaws.com", user="admin",
                       passwd="cmpe295b", db="sahayata1")


def registerdb(username, emailid, phonenum):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO user_table (username, emailid, phonenum) VALUES(%s,%s,%s)""", (username, emailid, phonenum))
    conn.commit()
    cursor.execute("""SELECT userid FROM user_table WHERE username = %s""", [username])
    userid = cursor.fetchone()
    cursor.close()
    response = {'userid': userid}
    conn.close()
    return jsonify(response)
