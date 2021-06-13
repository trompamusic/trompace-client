from .templates import subscription_create

MEDIA_OBJECT_SUBSCRIPTION = '''MediaObjectCreateMutation {{
      identifier
    }}'''


def subscription_media_object():
    args = {}
    return subscription_create(args, MEDIA_OBJECT_SUBSCRIPTION)