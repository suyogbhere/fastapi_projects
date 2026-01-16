"""create users table

Revision ID: 65b70d238f9e
Revises: 
Create Date: 2026-01-07 23:33:59.182780

"""
from typing import Sequence, Union

from alembic import op   
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65b70d238f9e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", sa.INTEGER, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("email",sa.String,nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
