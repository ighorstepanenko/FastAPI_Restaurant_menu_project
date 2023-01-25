"""First

Revision ID: f599b21ecee3
Revises: 
Create Date: 2023-01-26 02:01:21.287146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f599b21ecee3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_menus_id', table_name='menus')
    op.drop_table('menus')
    op.drop_index('ix_dishes_id', table_name='dishes')
    op.drop_table('dishes')
    op.drop_index('ix_submenus_id', table_name='submenus')
    op.drop_table('submenus')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('submenus',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('menu_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['menu_id'], ['menus.id'], name='submenus_menu_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='submenus_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_submenus_id', 'submenus', ['id'], unique=False)
    op.create_table('dishes',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('menu_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('submenu_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('price', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['menu_id'], ['menus.id'], name='dishes_menu_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['submenu_id'], ['submenus.id'], name='dishes_submenu_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='dishes_pkey')
    )
    op.create_index('ix_dishes_id', 'dishes', ['id'], unique=False)
    op.create_table('menus',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='menus_pkey')
    )
    op.create_index('ix_menus_id', 'menus', ['id'], unique=False)
    # ### end Alembic commands ###