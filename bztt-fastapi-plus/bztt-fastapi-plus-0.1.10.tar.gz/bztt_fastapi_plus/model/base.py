from sqlalchemy import Column, String, Text,TIMESTAMP, text,Index, DECIMAL,Float, Date ,BigInteger ,Integer,DateTime,TEXT
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT, TINYINT,VARCHAR


from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class Base(DeclarativeBase):
    """
    基础Model模型对象
    """
    __abstract__ = True

    id = Column(BIGINT(20), primary_key=True, comment='序号')
    parent_id = Column(BIGINT(20), nullable=False, server_default=text("0"), comment='父序号')
    type = Column(INTEGER(11), nullable=False, server_default=text("0"), comment='类型')
    sort = Column(INTEGER(11), nullable=False, server_default=text("0"), comment='排序')
    status = Column(TINYINT(2), nullable=False, server_default=text("0"), comment='状态')
    is_deleted = Column(TINYINT(1), nullable=False, server_default=text("0"), comment='软删')
    created_by = Column(BIGINT(20), nullable=False, server_default=text("0"), comment='创建人')
    created_time = Column(TIMESTAMP, nullable=False, server_default=text("current_timestamp()"), comment='创建时间')
    updated_by = Column(BIGINT(20), nullable=False, server_default=text("0"), comment='更新人')
    updated_time = Column(TIMESTAMP, nullable=False, server_default=text("current_timestamp() ON UPDATE current_timestamp()"), comment='更新时间')
    name = Column(String(255), nullable=False, server_default=text("''"), comment='名称')

    search = Column(LONGTEXT, comment='搜索')
