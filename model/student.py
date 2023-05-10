from config.config import meta
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String, Integer

student = Table(
        "tb_students",meta,
        Column("id", Integer, primary_key=True),
        Column("firstname", String(50)),
        Column("lastname", String(50)),
        Column("mail", String(50))
    )

