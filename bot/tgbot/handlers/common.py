from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tgbot.services.repository import Repo
from tgbot.handlers.authentication.authentication import authentication_start


async def command_start(msg: types.Message, repo: Repo, state: FSMContext):
    await state.finish()
    #
    user_id = msg.from_user.id
    if not await repo.check_user_is_exists(user_id):
        await authentication_start(msg)
    else:
        await msg.answer("<b>Вы уже аутентифицированы в системе :)</b>")


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start"], state="*")
