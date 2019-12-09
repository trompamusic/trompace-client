class UnsupportedLanguageException(Exception):
    def __init__(self, language):
        self().__init__("Languauage {} is not a supported language. See {}".format(language, "trompace.constants.SUPPORTED_LANGUAGES"))
