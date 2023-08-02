import inspect

import pymysql.err
from fastapi import HTTPException


def db_handler(func):
    def decorator_exception(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except pymysql.err.DatabaseError or pymysql.err.InternalError or pymysql.err.Warning or pymysql.err.OperationalError:
            raise HTTPException(status_code=500, detail=" DB server error\nTry again later...")
        except pymysql.err.NotSupportedError or pymysql.err.IntegrityError or pymysql.err.DataError or pymysql.err.ProgrammingError:
            raise HTTPException(status_code=400, detail="DB client error\n")
        except Exception as ex:
            raise HTTPException(status_code=400, detail="Sorry,DB error occurred..\n")

    return decorator_exception


def error_handler(func):
    async def decorator_exception(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return await result
        except FileNotFoundError or PermissionError or IOError as err:
            raise HTTPException(status_code=400, detail=str(err))
        except Exception:
            raise HTTPException(status_code=400, detail="internal server error, try again later...")

    return decorator_exception
