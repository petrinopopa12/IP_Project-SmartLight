from db_conn import get_db_connection
from flask import Blueprint, request
from auth import login_required

usage= Blueprint('usage', __name__)

@usage.route('/usage', methods=['GET'])
@login_required
def get_usage():
    conn = get_db_connection()
    rows = conn.execute('SELECT kw, data FROM current_usage ORDER BY id DESC').fetchone()
    result = dict(rows)
    conn.close()
    return result