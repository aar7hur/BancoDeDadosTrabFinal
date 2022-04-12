from bancodedadostrabfinal.main.config import Config
from psycopg2 import pool
from psycopg2.extras import RealDictConnection

_poolConnectionPostgres = None


def poolConnectionComposer() -> pool.ThreadedConnectionPool:
    global _poolConnectionPostgres

    config = Config()

    if _poolConnectionPostgres is None:
        _poolConnectionPostgres = pool.ThreadedConnectionPool(
            config.database.minConnection,
            config.database.maxConnection,
            user=config.database.user,
            password=config.database.password,
            host=config.database.host,
            port=config.database.port,
            database=config.database.database,
            connection_factory=RealDictConnection,
        )

    return _poolConnectionPostgres
