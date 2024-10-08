from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:
    def __init__(self, path_id: int, start_location: Habitat, species: str,destination: Habitat,duration: Optional[int] = None):
        self.path_id = path_id
        self.duration = duration or None
        self.start_location = start_location
        self.species = species
        self.destination = destination
    def get_migration_path_by_id(path_id: int) -> MigrationPath:
        pass
    def get_migration_path_details(path_id) -> dict:
        pass
    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass
    def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:
        pass
    def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
        pass
    def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:
        pass
