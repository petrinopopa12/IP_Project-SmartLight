from db_conn import get_db_connection
from flask import Blueprint, request
from auth import login_required


detect = Blueprint('detect', __name__)

@detect.route('/detect', methods=['PUT'])
@login_required
def set_detect():
    conn = get_db_connection()
    data = request.get_json(force=True)
    newMotion = data['motion']
    newTime = data['time1']
    rows = conn.execute('INSERT INTO detect(motion, time1) VALUES (?,?)', (newMotion, newTime)).fetchall()
    conn.commit()
    conn.close()
    return {'message':'Detect set successfully!'}


@detect.route('/detect', methods=['GET'])
@login_required
def get_detect():
    conn = get_db_connection()
    rows = conn.execute('SELECT motion, time1 FROM detect ORDER BY id DESC').fetchone()
    result = dict(rows)
    conn.close()
    return result