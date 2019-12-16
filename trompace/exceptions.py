class UnsupportedLanguageException(Exception):
    def __init__(self, language):
        super().__init__("Languauage {} is not a supported language. See {}".format(language, "trompace.constants.SUPPORTED_LANGUAGES"))

class IDNotFoundException(Exception):
    def __init__(self, object):
        super().__init__("{} ID not found".format(object))

class QueryException(Exception):
    def __init__(self, errors):
        error_str = "\n"
        for i, error in enumerate(errors):
            error_str+="{}. {}\n".format(1, error['message'])
        super().__init__("Query error {} occured".format(error_str))
