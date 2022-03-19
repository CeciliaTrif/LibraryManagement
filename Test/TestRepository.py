from Domain.Entity import Entity
from Repository.FileRepository import FileRepository
from Test.Utils import clear_file


def test_add_repository():
    clear_file("repository-test.txt")
    entities_repository = FileRepository("repository-test.txt")

    entity1 = Entity('1')

    entities_repository.add(entity1)
    assert len(entities_repository.get_all()) == 1
    added = entities_repository.get_by_id('1')
    assert added is not None
    assert added.entity_id == '1'

    try:
        entity2 = Entity('1')
        entities_repository.add(entity2)
        assert False
    except Exception:
        assert True

