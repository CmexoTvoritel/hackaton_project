import asyncio
from typing import List
from random import shuffle
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
            kb = types.InlineKeyboardMarkup()
            start_lec = types.InlineKeyboardButton(
                text="Начать лекцию",
                callback_data="start_lec"
            )
            kb.add(start_lec)
            await msg.answer(
                text=text,
                reply_markup=kb
            )
            #


async def start_lec(call: types.CallbackQuery, repo: Repo):
    lecture_id = 1

    q_ids = await repo.get_question_ids_by_lec_id(lecture_id)

    kb = types.InlineKeyboardMarkup()
    i = 1
    for q_id in q_ids:
        q = types.InlineKeyboardButton(
            text=f"{i} вопрос",
            callback_data=f"question_{i}_{q_id}"
        )
        kb.add(q)
        i += 1

    await call.message.edit_reply_markup(
        reply_markup=kb
    )
    await call.answer()

def create_answer_kb(btn_texts: List[str], q_id: int):
    # создаёт клаву из ответов по переданному списку ответов
    # 1 элемент списка верный
    kb = types.InlineKeyboardMarkup()
    btns = [
        types.InlineKeyboardButton(
            text=btn_texts[0],
            callback_data=f"q_{q_id}_true"
        )
    ]
    for answer in btn_texts[1:]:
        btns.append(
            types.InlineKeyboardButton(
                text=answer,
                callback_data=f"q_{q_id}_false"
            )
        )
    shuffle(btns)
    return kb.add(*btns)

async def send_question(call: types.CallbackQuery, repo: Repo):

    # по хорошему из БД подтягивается вопрос
    # текст вопроса / правильные ответ / другие варианты ответов / группы, у которых
    # сейчас лекция (студентам которых нужно кинуть вопрос)

    call_data = call.data
    q_id = int(call_data.split("_")[-1])
    group_names = await repo.get_group_names_by_q_id(q_id)

    q_data = await repo.get_question_data_by_q_id(q_id)
    q_text = q_data[0]
    q_answers = q_data[1]

    kb = create_answer_kb(q_answers, q_id)

    for group_name in group_names:
        users = await repo.get_users_tg_ids_by_group_name(group_name=group_name)
        for tg_id in users:
            try:
                await call.bot.send_message(
                    chat_id=tg_id,
                    text=q_text,
                    reply_markup=kb
                )
            except BotBlocked:
                pass
            await asyncio.sleep(MAILING_INTERVAL)
    await call.answer()


async def student_answer(call: types.CallbackQuery, repo: Repo):
    call_data = call.data.split("_")
    q_id = int(call_data[1])
    t_or_f = call_data[2]
    user_id = await  repo.get_user_id_by_tg_id(call.from_user.id)
    #
    if t_or_f == 'true':
        await repo.save_student_answer(q_id, user_id, True)
        await call.message.edit_text(
            text=call.message.text + "\n\n✅ Правильно!"
        )
    else:
        await repo.save_student_answer(q_id, user_id, False)
        await call.message.edit_text(
            text=call.message.text + "\n\n🔻 Неправильный ответ :("
        )
    await call.answer()

def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start"], state="*")
    dp.register_callback_query_handler(
        start_lec, text="start_lec", user_id=1333495909)
    dp.register_callback_query_handler(
        send_question, text_startswith="question_", user_id=1333495909)
    dp.register_callback_query_handler(
        student_answer, text_startswith="q_")
