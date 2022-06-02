"""populate_category_table

Revision ID: 5bc0cee5ef94
Revises: d84dff7e325b
Create Date: 2022-06-02 17:04:47.202929

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql import table
from sqlalchemy import String, Integer
from app import models as tb

# revision identifiers, used by Alembic.
revision = '5bc0cee5ef94'
down_revision = 'd84dff7e325b'
branch_labels = None
depends_on = None

def upgrade():
    table = tb.Category.__tablename__
    
    category_table = sa.table(
        table,
        sa.Column("category", String),
        sa.Column("industry_id", Integer)
    )

    op.bulk_insert(category_table, 
    [
        {"category":"Aircraft Dispatcher", "industry_id":13},
        {"category":"Aircraft Mechanic", "industry_id":13},
        {"category":"Airline Pilot", "industry_id":13},
        {"category":"Air Marshall", "industry_id":13},
        {"category":"Flight Attendant", "industry_id":13},
        {"category":"Traffic Air Controller", "industry_id":13},
        {"category":"Actor", "industry_id":14},
        {"category":"Museum Jobs", "industry_id":14},
        {"category":"Music Condutor", "industry_id":14},
        {"category":"Accountant", "industry_id":15},
        {"category":"Administrative Assistant/Secretary", "industry_id":15},
        {"category":"Advertising", "industry_id":19},
        {"category":"Financial", "industry_id":15},
        {"category":"Operations", "industry_id":15},
        {"category":"Management", "industry_id":15},
        {"category":"Consultancy", "industry_id":15},
        {"category":"Financial Advisor", "industry_id":15},
        {"category":"Goverment", "industry_id":15},
        {"category":"Human Resources", "industry_id":15},
        {"category":"Insurance Agent", "industry_id":15},
        {"category":"Investment Banker", "industry_id":15},
        {"category":"Lawyer", "industry_id":15},
        {"category":"Teaching", "industry_id":17},
        {"category":"Police Office", "industry_id":18},
        {"category":"Doctor", "industry_id":20},
        {"category":"Forensic Psychologist", "industry_id":20},
        {"category":"Nurse", "industry_id":20},
        {"category":"Midwife", "industry_id":20},
        {"category":"Veterinarian", "industry_id":20},
        {"category":"Psychologist", "industry_id":20},
        {"category":"Waiter", "industry_id":23},
        {"category":"Sales", "industry_id":21},
        {"category":"Backend Developer", "industry_id":22},
        {"category":"Systems Administrator", "industry_id":22},
        {"category":"Software Engineer", "industry_id":22},
        {"category":"Developer", "industry_id":22},
        {"category":"Architect", "industry_id":16},

        {"category":"Engineering", "industry_id":24},
        {"category":"Construction", "industry_id":16},
        {"category":"Health & Social", "industry_id":20},
        {"category":"Education", "industry_id":17},
        {"category":"Legal Occupations", "industry_id":18},
        {"category":"IT Occupations", "industry_id":22},
        {"category":"Catering", "industry_id":23},
        {"category":"Other", "industry_id":25},
    ])

def downgrade():
        op.execute("Delete from category")
