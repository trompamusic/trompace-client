class UnsupportedLanguageException(Exception):
    def __init__(self, language):
        super().__init__("Language {} is not a supported language. See trompace.constants.SUPPORTED_LANGUAGES".format(language))


class InvalidActionStatusException(Exception):
    def __init__(self, actionstatus):
        super().__init__("ActionStatusType {} is not a valid actionStatus. See trompace.constants.ActionStatusType".format(actionstatus))

class UnsupportedActionStatusException(Exception):
    def __init__(self, actionstatus):
        super().__init__("{} is not a supported action status. See {}".format(actionstatus,
                                                                                    "trompace.constants.SUPPORTED_ACTIONSTATUS_TYPES"))

class IDNotFoundException(Exception):
    def __init__(self, object):
        super().__init__("{} ID not found".format(object))


class NotAMimeTypeException(ValueError):
    def __init__(self, object):
        super().__init__("{} Not a valid mimetype".format(object))


class ConfigRequirementException(Exception):
    def __init__(self, object):
        super().__init__("{} not found in configuration file".format(object))


class ValueNotFound(Exception):
    def __init__(self, object):
        super().__init__("{} value not found".format(object))


class QueryException(Exception):
    def __init__(self, errors):
        error_str = "\n"
        for i, error in enumerate(errors):
            error_str += "{}. {}\n".format(1, error['message'])
        super().__init__("Query error {} occurred".format(error_str))
