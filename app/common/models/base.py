from .uuid import UUIDModel
from .create_update_time import CreateUpdateTime


class BaseModel(UUIDModel, CreateUpdateTime):
    """
    Abstract Base model with uuid pk and create and update time
    """


    class Meta:
        abstract = True
