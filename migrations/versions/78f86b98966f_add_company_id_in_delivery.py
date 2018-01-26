"""add company id in delivery

Revision ID: 78f86b98966f
Revises: 7ce1b661a69d
Create Date: 2018-01-26 09:11:43.068877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78f86b98966f'
down_revision = '7ce1b661a69d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('delivery', sa.Column('company_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'delivery', 'company', ['company_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'delivery', type_='foreignkey')
    op.drop_column('delivery', 'company_id')
    # ### end Alembic commands ###