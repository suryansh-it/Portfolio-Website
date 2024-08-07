"""chnaged id names

Revision ID: 1df6603996ff
Revises: 1b3d77e69d88
Create Date: 2024-08-07 17:22:53.859876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1df6603996ff'
down_revision = '1b3d77e69d88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Blog_Data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('blog_id', sa.Integer(), nullable=False))
        batch_op.drop_column('id')

    with op.batch_alter_table('Comment_Data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('Comment_Data_blog_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Blog_Data', ['blog_id'], ['blog_id'])
        batch_op.drop_column('id')

    with op.batch_alter_table('Project_Data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('project_id', sa.Integer(), nullable=False))
        batch_op.drop_column('id')

    with op.batch_alter_table('Visitor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('visitor_id', sa.Integer(), nullable=False))
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Visitor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
        batch_op.drop_column('visitor_id')

    with op.batch_alter_table('Project_Data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
        batch_op.drop_column('project_id')

    with op.batch_alter_table('Comment_Data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('Comment_Data_blog_id_fkey', 'Blog_Data', ['blog_id'], ['id'])
        batch_op.drop_column('comment_id')

    with op.batch_alter_table('Blog_Data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Blog_Data_id_seq"\'::regclass)'), autoincrement=True, nullable=False))
        batch_op.drop_column('blog_id')

    # ### end Alembic commands ###