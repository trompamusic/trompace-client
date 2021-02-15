import enum

SUPPORTED_LANGUAGES = {"en", "es", "ca", "nl", "de", "fr"}


SUPPORTED_GENDER = {"male", "female", "other"}


class ActionStatusType(enum.Enum):
    ActiveActionStatus = enum.auto()
    CompletedActionStatus = enum.auto()
    FailedActionStatus = enum.auto()
    PotentialActionStatus = enum.auto()

    def __str__(self):
        return self.name


class ItemListOrderType(enum.Enum):
    ItemListOrderAscending = enum.auto()
    ItemListOrderDescending = enum.auto()
    ItemListUnordered = enum.auto()

    def __str__(self):
        return self.name
