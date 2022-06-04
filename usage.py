from db_conn import get_db_connection
from flask import Blueprint, request
from auth import login_required

usage= Blueprint('usage', __name__)

@usage.route('/usage', methods=['PUT'])
@login_required
def set_weather():
    conn = get_db_connection()
    data = request.get_json(force=True)
    newMeteo = data['meteo']
    newTime = data['time']
    rows = conn.execute('INSERT INTO weather(meteo, time) VALUES (?,?)', (newMeteo, newTime)).fetchall()
    conn.commit()
    conn.close()
    return {'message':'Weather set successfully!'}


@usage.route('/usage', methods=['GET'])
@login_required
def get_weather():
    conn = get_db_connection()
    rows = conn.execute('SELECT meteo, time FROM weather ORDER BY id DESC').fetchone()
    result = dict(rows)
    conn.close()
    return result