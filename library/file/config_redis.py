import configparser, os
from pathlib import Path
from typing import Optional

_REDIS_CONFIG_CACHE : Optional[tuple[str,str,str]] =None

def read_redis_config() -> tuple[str,str,str]:
    global _REDIS_CONFIG_CACHE
    if _REDIS_CONFIG_CACHE is None:
        base_path = Path(__file__).parent.parent.parent
        config_file = base_path / 'config' / 'redis_config_lofi.ini'

        redis_config = configparser.ConfigParser()
        redis_config.read(config_file,encoding='utf-8')

        redis_password = os.environ.get('redis_password') or redis_config.get('redis_setting', 'Password')
        redis_host = os.environ.get('redis_host') or redis_config.get('redis_setting', 'Host')
        redis_port = 6379 or redis_config.get('redis_setting', 'Port')

        _REDIS_CONFIG_CACHE = (redis_host, redis_port, redis_password)
    return _REDIS_CONFIG_CACHE

