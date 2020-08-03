import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
import settings


def build_connection_url():
    return "postgresql://{0}:{1}@{2}/{3}".format(
        settings.DB_USER, settings.DB_PASS, settings.DB_HOST, settings.DB_NAME
    )


eng = create_engine(build_connection_url())

Base = automap_base()
Base.prepare(eng, reflect=True)


class StaffMember(Base):
    __tablename__ = "staff_members"


metadata = sa.MetaData(bind=None)
staff_members = sa.Table("staff_members", metadata, autoload=True, autoload_with=eng)
