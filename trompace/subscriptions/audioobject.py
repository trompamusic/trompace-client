from .templates import subscription_create

AUDIO_OBJECT_SUBSCRIPTION = '''AudioObjectCreateMutation {{
      identifier
    }}'''


def subscription_audio_object():
    args = {}
    return subscription_create(args, AUDIO_OBJECT_SUBSCRIPTION)