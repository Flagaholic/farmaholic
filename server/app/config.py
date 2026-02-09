import os

CONFIG = {
    'DEBUG': os.getenv('DEBUG') == '1',

    # 'TEAMS': {
    #     f'Team #{i}': f'10.60.{i}.3'
    #     for i in range(0, 10)
    # },
    
    'FLAG_FORMAT': r'flag{[a-z0-9]{32}}',

    # 'SYSTEM_PROTOCOL': 'ructf_http',
    # 'SYSTEM_URL': 'http://monitor.ructfe.org/flags',
    # 'SYSTEM_TOKEN': '275_17fc104dd58d429ec11b4a5e82041cd2',

    # 'SYSTEM_PROTOCOL': 'forcad_tcp',
    # 'SYSTEM_HOST': '10.10.10.10',
    # 'SYSTEM_PORT': '31337',
    # 'TEAM_TOKEN': '4fdcd6e54faa8991',
    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_VALIDATOR': 'volgactf',
    # 'SYSTEM_HOST': 'final.volgactf.ru',
    # 'SYSTEM_SERVER_KEY': validators.volgactf.get_public_key('https://final.volgactf.ru'),
    'SYSTEM_PROTOCOL': 'hkcert_http',
    'SYSTEM_URL': 'http://10.2.60.1/api/ct/web/awd_race/race/38d769e349e4ee6e6d25aa4a2d0906f1/flag/robot/',
    'SYSTEM_TOKEN': '938a7af9cc469978e42d3f91e1a8e360',

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': 10,
    'SUBMIT_PERIOD': 1,
    'FLAG_LIFETIME': 5 * 60,

    # VOLGA: Don't make more than INFO_FLAG_LIMIT requests to get flag info,
    # usually should be more than SUBMIT_FLAG_LIMIT
    # 'INFO_FLAG_LIMIT': 10,

    # Password for the web interface. This key will be excluded from config
    # before sending it to farm clients.
    # ########## DO NOT FORGET TO CHANGE IT ##########
    'SERVER_PASSWORD': os.getenv('SERVER_PASSWORD') or '1234',

    # For all time-related operations
    'TIMEZONE': 'Asia/Hong_Kong',
}
