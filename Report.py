import json

import MySQLdb
from flask import jsonify

conn = MySQLdb.connect(host="sahayata1.cq3lebnygdgj.us-west-1.rds.amazonaws.com", user="admin",
                       passwd="cmpe295b", db="sahayata1")


def reportincident(lat, longi, userid, incident):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO incident_table (latitude, longitude, userid, incident) VALUES(%s,%s,%s,%s)""",
                   (lat, longi, int(userid), incident))
    conn.commit()
    cursor.execute("""SELECT incidentid FROM incident_table WHERE latitude = %s AND longitude = %s""", (lat, longi))
    incidentid = cursor.fetchone()
    cursor.close()
    response = {'incidentid': incidentid, 'message': 'Incident Reported'}
    return jsonify(response)


def getincidents():
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM incident_table""")
    incidentlist = cursor.fetchall()
    result = []
    for incident in incidentlist:
        i = {
            "incidentid": incident[0],
            "latitude": incident[1],
            "longitude": incident[2],
            "userid": incident[3],
            "incident": incident[4]
         }
        result.append(i)
    conn.close()
    return jsonify({'incidents':result})
