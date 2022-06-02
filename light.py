from db_conn import get_db_connection
from flask import Blueprint, request
from auth import login_required


light = Blueprint('light', __name__)

@light.route('/light/color', methods=['PUT'])
@login_required
def set_light():
    conn = get_db_connection()
    data = request.get_json(force=True)
    newColor = data['color']
    newTime = data['time']
    rows = conn.execute('INSERT INTO light(color, time) VALUES (?,?)', (newColor, newTime)).fetchall()
    conn.commit()
    conn.close()
    return {'message':'Light set successfully!'}


@light.route('/light/color', methods=['GET'])
@login_required
def get_light():
    conn = get_db_connection()
    rows = conn.execute('SELECT color, time FROM light ORDER BY id DESC').fetchone()
    result = dict(rows)
    conn.close()
    return result

