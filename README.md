# Автотест подключения к PostgreSQL (pytest)

Тестовое задание для стажёров: база данных и Python.

## Цель

Автотест проверяет, что:

1. Приложение может подключиться к PostgreSQL.
2. База отвечает на простейший SQL-запрос.
3. При неверных параметрах подключения тест не проходит.

Используемый запрос:

```sql
SELECT now();
```

## Стек

- Python 3.11+
- PostgreSQL
- pytest
- psycopg 3

## Структура проекта

```text
intern-db-test/
├── test_db_connection.py   # сам тест
├── requirements.txt        # зависимости
├── .gitignore
└── README.md
```

## Установка

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

## Параметры подключения

Параметры задаются через переменные окружения. Пароль в репозитории не хранится.

| Переменная | Значение по умолчанию | Описание |
|---|--|---|
| `DB_HOST` | `127.0.0.1` | Хост PostgreSQL |
| `DB_PORT` | `5432` | Порт PostgreSQL |
| `DB_NAME` | `postgres` | Имя базы |
| `DB_USER` | `postgres` | Пользователь |
| `DB_PASSWORD` | "" | Пароль пользователя |

### Windows PowerShell

```powershell
$env:DB_HOST="127.0.0.1"
$env:DB_PORT="5432"
$env:DB_NAME="postgres"
$env:DB_USER="postgres"
$env:DB_PASSWORD="YOUR_PASSWORD"
```

## Запуск теста

```bash
pytest -v
```

Результат при правильном пароле:

```text
test_db_connection.py::test_postgres_connection_and_select_now PASSED    [100%]
```

## Что проверяет тест

1. Открывает соединение через `psycopg.connect()`.
2. Выполняет `SELECT now()`.
3. Проверяет, что:
   - вернулся непустой результат;
   - значение имеет тип `datetime`.
4. Закрывает соединение после завершения тестовой сессии.


## Демонстрация падения теста

Чтобы проверить, что тест действительно реагирует на ошибку подключения,
нужно запустить его с неверным паролем.

Windows PowerShell:

```powershell
$env:DB_PASSWORD="wrong_password"
pytest -v
```

Результат:

```text
test_postgres_connection_and_select_now - psycopg.OperationalError: connection failed: connection to server at "127.0.0.1", port 5432 failed
```

Тест падает на этапе создания фикстуры, потому что не может установить соединение.

Причина ошибки - аутентификация:

```text
password authentication failed for user "postgres"
```
