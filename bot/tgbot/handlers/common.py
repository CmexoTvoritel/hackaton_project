import asyncio
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import BotBlocked
from tgbot.services.repository import Repo
from tgbot.handlers.authentication.authentication import authentication_start
from tgbot.data.config import MAILING_INTERVAL


async def command_start(msg: types.Message, repo: Repo, state: FSMContext):
    await state.finish()
    #
    user_id = msg.from_user.id
    if not await repo.check_user_is_exists(user_id):
        await authentication_start(msg)
    else:
        await msg.answer("<b>Вы уже аутентифицированы в системе :)</b>")
        #
        if msg.from_user.id == 1333495909:
            text = "Тестовая панель хакатона."
            #
            kb = types.InlineKeyboardMarkup()
            q_1 = types.InlineKeyboardButton(
                text="1 вопрос",
                callback_data="question_1"
            )
            kb.add(q_1)
            q_2 = types.InlineKeyboardButton(
                text="2 вопрос",
                callback_data="question_2"
            )
            kb.add(q_2)
            q_3 = types.InlineKeyboardButton(
                text="3 вопрос",
                callback_data="question_3"
            )
            kb.add(q_3)
            #
            await msg.answer(
                text=text,
                reply_markup=kb
            )


async def send_question(call: types.CallbackQuery, repo: Repo):
    kb = types.InlineKeyboardMarkup()
    if call.data[-1] == "1":
        q_text = "q_1"
        # TODO buttons
    elif call.data[-1] == "2":
        q_text = "q_2"
        # TODO buttons
    elif call.data[-1] == "3":
        q_text = "q_3"
        # TODO buttons

    group_name = "КТбо1-1"
    users = await repo.get_users_by_group_name(group_name=group_name)

    for tg_id in users:
        try:
            await call.bot.send_message(
                chat_id=tg_id,
                text=q_text,
                reply_markup=kb
            )
        except BotBlocked:
            pass
        #
        await asyncio.sleep(MAILING_INTERVAL)
    await call.answer()


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start"], state="*")
    dp.register_callback_query_handler(
        send_question, text_startswith="question_", user_id=1333495909)
