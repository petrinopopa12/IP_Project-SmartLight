from db_conn import get_db_connection
from flask import Blueprint, request
from auth import login_required

routine = Blueprint('light', __name__)

@routine.route('/light/routine', methods=['PUT'])
@login_required
def set_routine():
    conn = get_db_connection()
    data = request.get_json(force=True)
    newStart = data['start']
    newEnd = data['end']
    newColor = data['color']
    newLightLevel = data['light_level']
    rows = conn.execute('INSERT INTO routine(start, end, color, light_level) VALUES (?,?,?,?)', (newStart, newEnd, newColor, newLightLevel)).fetchall()
    conn.commit()
    conn.close()
    return {'message':'Routine set successfully!'}


@routine.route('/light/routine', methods=['GET'])
@login_required
def get_routine():
    conn = get_db_connection()
    rows = conn.execute('SELECT start, end, color, light_level FROM routine ORDER BY id DESC').fetchone()
    result = dict(rows)
    conn.close()
    return result
