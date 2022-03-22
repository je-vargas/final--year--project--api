"""change tel type on contact details

Revision ID: d3cb7b1f1aab
Revises: 03b906fc289e
Create Date: 2022-03-22 16:20:56.817735

"""
from alembic import op
import sqlalchemy as sa
from app.models import ContactDetails


# revision identifiers, used by Alembic.
revision = 'd3cb7b1f1aab'
down_revision = '03b906fc289e'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("contactDetails", "telephoneNumber", type_= sa.String)


def downgrade():
    op.alter_column("contactDetails", "telephoneNumber", type_= sa.TIMESTAMP(timezone=True), nullable=False)
