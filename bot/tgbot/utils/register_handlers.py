from tgbot.handlers.common import register_handlers_common
from tgbot.handlers.authentication.authentication import register_handlers_authentication


def register_handlers(dp):
    register_handlers_common(dp)
    register_handlers_authentication(dp)
