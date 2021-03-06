"""empty message

Revision ID: 17ee00ed83a3
Revises: 
Create Date: 2021-11-22 20:14:08.748948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17ee00ed83a3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audience',
    sa.Column('idAudience', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('amount_of_places', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('idAudience')
    )
    op.create_table('user',
    sa.Column('idUser', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.Column('surname', sa.String(length=45), nullable=True),
    sa.Column('username', sa.String(length=45), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('idUser')
    )
    op.create_table('reservation',
    sa.Column('idReservation', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=45), nullable=True),
    sa.Column('from_date', sa.DateTime(), nullable=True),
    sa.Column('to_date', sa.DateTime(), nullable=True),
    sa.Column('User_idUser', sa.Integer(), nullable=True),
    sa.Column('Audience_idAudience', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Audience_idAudience'], ['audience.idAudience'], ),
    sa.ForeignKeyConstraint(['User_idUser'], ['user.idUser'], ),
    sa.PrimaryKeyConstraint('idReservation')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    op.drop_table('user')
    op.drop_table('audience')
    # ### end Alembic commands ###
