"""created the ingredients table

Revision ID: 816087530444
Revises: 
Create Date: 2024-04-21 03:07:06.962845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '816087530444'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredient',
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('ingredient', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('ingredient_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ingredient')
    # ### end Alembic commands ###
