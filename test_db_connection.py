import os
from datetime import datetime

import pytest
import psycopg


DB_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": int(os.getenv("DB_PORT", "5432")),
    "dbname": os.getenv("DB_NAME", "postgres"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),
}


@pytest.fixture(scope="session")
def db_connection():
    connection = psycopg.connect(
        connect_timeout=5,
        **DB_CONFIG,
    )

    yield connection

    connection.close()


def test_postgres_connection_and_select_now(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT now()")
        result = cursor.fetchone()

    assert result is not None, "Запрос не вернул результат"
    assert result[0] is not None, "Результат запроса пустой"
    assert isinstance(result[0], datetime), "Ожидался тип datetime"