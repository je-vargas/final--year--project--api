"""populate_industry

Revision ID: d84dff7e325b
Revises: 0ce3fd999bd6
Create Date: 2022-06-02 17:03:08.640892

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql import table
from sqlalchemy import String
from app import models as tb

# revision identifiers, used by Alembic.
revision = 'd84dff7e325b'
down_revision = '0ce3fd999bd6'
branch_labels = None
depends_on = None

def upgrade():
    industry_table = table(
            tb.Industry.__tablename__,
            sa.Column("industry", String)
        )

    op.bulk_insert(industry_table, 
        [
            {"industry":"Aviation"},
            {"industry":"Arts"},
            {"industry":"Business"},
            {"industry":"Construction"},
            {"industry":"Education"},
            {"industry":"Law Enforcement"},
            {"industry":"Media"},
            {"industry":"Medical"},
            {"industry":"Service Industry"},
            {"industry":"Technology"},
            {"industry":"Hospitality"},
            {"industry":"Engineering"},
            {"industry":"Other"},
        ])

def downgrade():
    op.execute("Delete from industry")