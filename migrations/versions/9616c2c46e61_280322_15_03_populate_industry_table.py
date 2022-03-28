"""280322_15:03_populate_cateogry_and_industry

Revision ID: 9616c2c46e61
Revises: 8a1bd54c60b8
Create Date: 2022-03-28 15:30:31.727814

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

from app import models as tb



# revision identifiers, used by Alembic.
revision = '9616c2c46e61'
down_revision = '8a1bd54c60b8'
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
    ])
    
def downgrade():
    
    op.execute("Delete from industry")
