import os
import sys

# เพิ่ม Path ของโปรเจคลงใน sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Import การเชื่อมต่อฐานข้อมูล
from app.config import DATABASE_URL
from app.database import Base

# Import Model ที่สร้างไว้ทั้งหมด
from app.models.user import User

# การตั้งค่าการ Log และการ Migration
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# การตั้งค่า Alembic Config
config = context.config

# Override sqlalchemy.url ด้วย DATABASE_URL
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# ตั้งค่าการ Log
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ตั้งค่า Metadata สำหรับ Auto-Generate
target_metadata = Base.metadata

# ฟังก์ชันสำหรับการ Migration แบบออฟไลน์
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# ฟังก์ชันสำหรับการ Migration แบบออนไลน์
def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# เลือกรันแบบออนไลน์หรือออฟไลน์
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
