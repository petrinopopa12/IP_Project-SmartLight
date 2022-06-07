from db_conn import get_db_connection

def get_status():
    light_level = get_db_connection().execute(
        '''SELECT light_level
        FROM light
        ORDER BY id_lb DESC'''
    ).fetchone()

    color = get_db_connection().execute(
        '''SELECT color
        FROM light
        ORDER BY id_lb DESC'''
    ).fetchone()
    
    time = get_db_connection().execute(
        '''SELECT time
        FROM light
        ORDER BY id_lb DESC'''
    ).fetchone()

    if light_level is None or color is None:
        return {'status': 'Query failed'}
    
    return {
        'data': {
            'light_level': light_level['light_level'],
            'color': color['color'],
            'time': time['time'],
        }
    }