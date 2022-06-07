from db_conn import get_db_connection
from flask import Blueprint, request
from auth import login_required
import time

light = Blueprint('light', __name__)

@light.route('/light', methods=['POST'])
#@login_required
def set_light():
    conn = get_db_connection()
    data = request.get_json(force=True)
    newColor = data['color']
    newLevel = data['light_level']
    with open('logs.txt', 'a') as f:
        rows = conn.execute('INSERT INTO light(color, light_level) VALUES (?,?)', (newColor, newLevel)).fetchall()
        conn.commit()
        f.write(f"Manual light bulb input: color={newColor} light_level={newLevel} at {time.asctime()}\n")

        time.sleep(10)
        
        rows = conn.execute('INSERT INTO light(color, light_level) VALUES (?,?)', (newColor, newLevel/2)).fetchall()
        conn.commit()
        f.write(f"Automatic light level reduction: light_level={newLevel/2} at {time.asctime()}\n")

    conn.close()
    return {'message':'Light set successfully!'}


@light.route('/light', methods=['GET'])
#@login_required
def get_light():
    conn = get_db_connection()
    rows = conn.execute('SELECT id_lb, color, light_level, time FROM light ORDER BY id_lb DESC').fetchone()
    result = dict(rows)
    conn.close()
    return result

