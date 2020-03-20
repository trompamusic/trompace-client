import enum

SUPPORTED_LANGUAGES = ["en", "es", "ca", "nl", "de", "fr"]


class ActionStatusType(enum.Enum):
    ActiveActionStatus = enum.auto()
    CompletedActionStatus = enum.auto()
    FailedActionStatus = enum.auto()
    PotentialActionStatus = enum.auto()

    def __str__(self):
        return self.name
