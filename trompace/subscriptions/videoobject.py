from .templates import subscription_create

VIDEO_OBJECT_SUBSCRIPTION = '''VideoObjectCreateMutation {{
      identifier
    }}'''


def subscription_media_object():
    args = {}
    return subscription_create(args, VIDEO_OBJECT_SUBSCRIPTION)