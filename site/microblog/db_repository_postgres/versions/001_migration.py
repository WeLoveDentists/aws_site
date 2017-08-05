from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
apache_logs = Table('apache_logs', pre_meta,
    Column('ip', TEXT),
    Column('date', TEXT),
    Column('method', TEXT),
    Column('protocol', TEXT),
    Column('http_status', TEXT),
    Column('user_agent_details', TEXT),
)

common_compounds = Table('common_compounds', pre_meta,
    Column('chemical_name', TEXT),
    Column('chemical_formula', TEXT),
    Column('common_name', TEXT),
    Column('source_and_description', TEXT),
)

common_inventions = Table('common_inventions', pre_meta,
    Column('time_period', TEXT),
    Column('invention', TEXT),
)

common_misspellings = Table('common_misspellings', pre_meta,
    Column('word', TEXT),
    Column('common_misspellings', TEXT),
)

inventions_timeline = Table('inventions_timeline', pre_meta,
    Column('time_period', TEXT),
    Column('invention', TEXT),
)

inventions_timeline_with_image_links = Table('inventions_timeline_with_image_links', pre_meta,
    Column('image_link', TEXT),
    Column('time_period', TEXT),
    Column('invention', TEXT),
)

organization_details = Table('organization_details', pre_meta,
    Column('anchor', TEXT),
    Column('address', TEXT),
    Column('city', TEXT),
    Column('state', TEXT),
    Column('zip', TEXT),
    Column('telephone', TEXT),
    Column('fax', TEXT),
    Column('ein', TEXT),
    Column('award', TEXT),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['apache_logs'].drop()
    pre_meta.tables['common_compounds'].drop()
    pre_meta.tables['common_inventions'].drop()
    pre_meta.tables['common_misspellings'].drop()
    pre_meta.tables['inventions_timeline'].drop()
    pre_meta.tables['inventions_timeline_with_image_links'].drop()
    pre_meta.tables['organization_details'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['apache_logs'].create()
    pre_meta.tables['common_compounds'].create()
    pre_meta.tables['common_inventions'].create()
    pre_meta.tables['common_misspellings'].create()
    pre_meta.tables['inventions_timeline'].create()
    pre_meta.tables['inventions_timeline_with_image_links'].create()
    pre_meta.tables['organization_details'].create()
