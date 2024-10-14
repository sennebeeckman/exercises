import re
from abc import ABC, abstractmethod
class StorageDevice:

    def __init__(self, block_count, block_size):
        self.__block_size = block_size
        self.__available_blocks = {block_number for block_number in range(block_count)}
        self.__used_blocks = set()
    
    @property
    def available_block_count(self):
        return len(self.__available_blocks)
    
    @property
    def used_block_count(self):
        return len(self.__used_blocks)
    
    @property
    def total_block_count(self):
        return self.available_block_count + self.used_block_count
    
    @property
    def block_size(self):
        return self.__block_size
    
    def allocate(self, block_count):
        if self.available_block_count < block_count:
            raise RuntimeError
        
        list_available_blocks = list(self.__available_blocks)
        to_use_available_blocks = list_available_blocks[:block_count]

        self.__available_blocks = set(list_available_blocks[block_count:])
        self.__used_blocks.update(to_use_available_blocks)
        return to_use_available_blocks

    def free(self, blocks):
        if not all(block in self.__used_blocks for block in blocks):
            raise RuntimeError
        
        [self.__used_blocks.remove(block) for block in blocks]
        self.__available_blocks.update(blocks)
    
class Entity(ABC):
    def __init__(self, storage, name):
        self.__storage = storage
        if not Entity.is_valid_name(name):
            raise RuntimeError
        self.__name = name

    @staticmethod
    def is_valid_name(name):
        return bool(re.fullmatch('[a-zA-Z0-9.]{1,16}', name))

    
    @property
    def storage(self):
        return self.__storage
    
    @property
    @abstractmethod
    def size_in_blocks(self):
        pass

    @property
    def size_in_bytes(self):
        return self.size_in_blocks * self.storage.block_size
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if not Entity.is_valid_name(new_name):
            raise RuntimeError
        self.__name = new_name

    @abstractmethod
    def clear(self):
        pass


class File(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__used_blocks_storage = []

    @property
    def size_in_blocks(self):
        return len(self.__used_blocks_storage)
    
    def grow(self, block_count):
        self.__used_blocks_storage.extend(self.storage.allocate(block_count))

    def clear(self):
        self.storage.free(self.__used_blocks_storage)
        self.__used_blocks_storage = []
        
class Directory(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__children = []

    @property
    def size_in_blocks(self):
        sum = 0
        for entity in self.__children:
            if isinstance(entity, File):
                sum += entity.size_in_blocks
            else:
                sum += entity.size_in_blocks
        return sum
        

    def add(self, entity):
        self.__children.append(entity)

    def clear(self):
        for entity in self.__children:
            if isinstance(entity, File):
                entity.clear()
            else:
                entity.clear()


    