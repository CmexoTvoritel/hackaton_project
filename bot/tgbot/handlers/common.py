from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tgbot.services.repository import Repo


async def command_start(msg: types.Message, repo: Repo, state: FSMContext):
    await state.finish()
    await repo.add_user(msg.from_user.id)
    await msg.reply("Hello, user!")


async def command_cancel(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.reply("Action canceled.")


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start"], state="*")
    dp.register_message_handler(command_cancel, commands=["cancel"], state="*")
