"""Fixed comments creator

Revision ID: 9cabad87d9c9
Revises: 684076d8ffe2
Create Date: 2021-09-13 16:45:22.342603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cabad87d9c9'
down_revision = '684076d8ffe2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('creator_id', sa.Integer(), nullable=False))
    op.drop_constraint('comments_author_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'users', ['creator_id'], ['id'])
    op.drop_column('comments', 'author_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_author_id_fkey', 'comments', 'users', ['author_id'], ['id'])
    op.drop_column('comments', 'creator_id')
    # ### end Alembic commands ###
