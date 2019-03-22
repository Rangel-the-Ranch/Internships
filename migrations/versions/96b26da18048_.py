"""empty message

Revision ID: 96b26da18048
Revises: 05c3a7da4ea8
Create Date: 2019-03-19 15:51:43.040670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96b26da18048'
down_revision = '05c3a7da4ea8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Company', sa.Column('password', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Company', 'password')
    # ### end Alembic commands ###
