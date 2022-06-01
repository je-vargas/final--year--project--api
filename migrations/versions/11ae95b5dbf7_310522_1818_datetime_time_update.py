"""310522_1818_DateTime_Time_update

Revision ID: 11ae95b5dbf7
Revises: 2ae43caee49f
Create Date: 2022-05-31 18:20:36.517636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11ae95b5dbf7'
down_revision = '2ae43caee49f'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("userAccount", "dateCreated", type_= sa.DateTime)
    op.alter_column("userAccount", "lastLogin", type_= sa.DateTime)
    op.alter_column("jobs", "startDate", type_= sa.Date)
    op.alter_column("jobs", "endDate", type_= sa.Date)
    op.alter_column("jobs", "applicationDeadLine", type_= sa.Date)


def downgrade():
    op.alter_column("", "", type_= sa.String)
    op.alter_column("userAccount", "dateCreated", type_= sa.TIMESTAMP)
    op.alter_column("userAccount", "lastLogin", type_= sa.TIMESTAMP)
    op.alter_column("jobs", "startDate", type_= sa.TIMESTAMP)
    op.alter_column("jobs", "endDate", type_= sa.TIMESTAMP)
    op.alter_column("jobs", "applicationDeadLine", type_= sa.TIMESTAMP)