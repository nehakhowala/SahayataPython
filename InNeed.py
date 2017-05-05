import MySQLdb
from flask import jsonify

conn = MySQLdb.connect(host="sahayata1.cq3lebnygdgj.us-west-1.rds.amazonaws.com", user="admin",
                       passwd="cmpe295b", db="sahayata1")


def getuserlist(json_dict):
    cursor = conn.cursor()
    cursor.execute("""SELECT username, phonenum FROM user_table""")
    contactlist = cursor.fetchall()
    print(contactlist)
    result = []
    for contact in contactlist:
        i = {
            "username": contact[0],
            "phonenum": contact[1]
        }
        result.append(i)
    conn.close()
    print(result)
    return jsonify({"users":result})
