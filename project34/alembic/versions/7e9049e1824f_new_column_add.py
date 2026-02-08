"""Phone column add

Revision ID: 7e9049e1824f
Revises: 65b70d238f9e
Create Date: 2026-01-16 23:19:07.828939

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e9049e1824f'
down_revision: Union[str, Sequence[str], None] = '65b70d238f9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("users", sa.Column("phone", sa.Integer()))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users",'phone')
