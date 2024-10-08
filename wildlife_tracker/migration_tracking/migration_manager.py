from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath
class MigrationManager:
    def __init__(self) -> None:
        migrations: dict[int, Migration] = {}
        paths: dict[int, MigrationPath] = {}
        migration_path: MigrationPath
    def cancel_migration(migration_id: int) -> None:
        pass
    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass
    def get_migration_paths() -> list[MigrationPath]:
        pass
    def get_migrations() -> list[Migration]:
        pass
    def remove_migration_path(path_id: int) -> None:
        pass
    def schedule_migration(migration_path: MigrationPath) -> None:
        pass