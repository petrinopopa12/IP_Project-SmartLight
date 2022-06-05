from db_conn import get_db_connection

def get_status():
    light_bulb = get_db_connection().execute(
        '''SELECT light_level
        FROM light
        ORDER BY time DESC'''
    ).fetchone()

    current_usage = get_db_connection().execute(
        '''SELECT kw
        FROM current_usage
        ORDER BY data DESC'''
    ).fetchone()

    if light_bulb is None or current_usage is None:
        return {'status': 'Query failed'}
    
    return {
        'data': {
            'light_bulb': {
                'light_level' : light_bulb['light_level']
            },
            'current_usage': {
                'kw': current_usage['kw']
            }
        }
    }