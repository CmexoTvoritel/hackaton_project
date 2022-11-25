from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tgbot.services.repository import Repo
from tgbot.states.authentication import AuthenticationState
from validate_email import validate_email


async def authentication_start(msg: types.Message):
    text = "🔹 <b>Авторизация</b>\nВведите свою sfedu-почту..."
    #
    await msg.answer(text=text)
    await AuthenticationState.waiting_for_email.set()


async def email_writen(msg: types.Message, state: FSMContext):
    if (validate_email(msg.text) == False) or (msg.text[-9:] != "@sfedu.ru"):
        await msg.answer(text="🔻 Введите валидную электронную почту sfedu...")
        return
    await state.update_data(email=msg.text)
    text = "🔹 <b>Авторизация</b>\nВведите своё имя..."
    #
    await msg.answer(text=text)
    await AuthenticationState.next()


async def name_writen(msg: types.Message, state: FSMContext):
    if len(msg.text) > 60:
        await msg.answer(text="🔻 Длина имени не может превышать 60 символов.\nПожалуйста, попробуйте ещё раз...")
        return
    await state.update_data(name=msg.text)
    text = "🔹 <b>Авторизация</b>\nВведите свою фамилию..."
    #
    await msg.answer(text=text)
    await AuthenticationState.next()


async def surname_writen(msg: types.Message, state: FSMContext):
    if len(msg.text) > 60:
        await msg.answer(text="🔻 Длина фамилии не может превышать 60 символов.\nПожалуйста, попробуйте ещё раз...")
        return
    await state.update_data(surname=msg.text)
    text = "🔹 <b>Авторизация</b>\nВведите своё отчество..."
    #
    await msg.answer(text=text)
    await AuthenticationState.next()


async def patronymic_writen(msg: types.Message, state: FSMContext):
    if len(msg.text) > 60:
        await msg.answer(text="🔻 Длина отчества не может превышать 60 символов.\nПожалуйста, попробуйте ещё раз...")
        return
    await state.update_data(patronymic=msg.text)
    text = "🔹 <b>Авторизация</b>\nВведите свою группу (например КТбо1-7)"
    #
    await msg.answer(text=text)
    await AuthenticationState.next()


async def group_name_writen(msg: types.Message, repo: Repo, state: FSMContext):
    if len(msg.text) > 7:
        await msg.answer(text="🔻 Длина группы не может превышать 7 символов.\nПожалуйста, попробуйте ещё раз...")
        return

    tmp_gr_name = msg.text
    tmp_gr_name = tmp_gr_name[0].upper() + tmp_gr_name[1].upper() + \
        tmp_gr_name[2].lower() + tmp_gr_name[3].lower() + tmp_gr_name[-3:]

    await state.update_data(group_name=tmp_gr_name)
    #
    user_data = await state.get_data()
    email = user_data["email"]
    name = user_data["name"]
    surname = user_data["surname"]
    patronymic = user_data["patronymic"]
    group_name = msg.text
    #
    text = f"🔹 <b>Введённые данные:</b>\n\n<b>Почта:</b> {email}\n<b>ФИО:</b> {surname} {name} {patronymic}\n<b>Группа:</b> {group_name}"
    kb = types.InlineKeyboardMarkup()
    confirm_btn = types.InlineKeyboardButton(
        text="✅ Подтвердить",
        callback_data="confirm_user_data"
    )
    kb.add(confirm_btn)
    re_enter_btn = types.InlineKeyboardButton(
        text="🔁 Ввести заного",
        callback_data="re_enter_user_data"
    )
    kb.add(re_enter_btn)
    await msg.answer(
        text=text,
        reply_markup=kb
    )
    await AuthenticationState.next()


async def user_data_confirmed(call: types.CallbackQuery, repo: Repo, state: FSMContext):
    user_data = await state.get_data()
    tg_id = call.from_user.id
    email = user_data["email"]
    name = user_data["name"]
    surname = user_data["surname"]
    patronymic = user_data["patronymic"]
    group_name = user_data["group_name"]
    await repo.authenticate_user(tg_id, email, name, surname, patronymic, group_name)
    #
    await call.message.edit_text(text=call.message.text + "\n\n✅ Авторизация прошла успешно!")
    await call.answer()
    await state.finish()


async def re_enter_user_data(call: types.CallbackQuery):
    await authentication_start(call.message)
    await call.answer()


def register_handlers_authentication(dp: Dispatcher):
    dp.register_message_handler(
        email_writen, state=AuthenticationState.waiting_for_email)
    dp.register_message_handler(
        name_writen, state=AuthenticationState.waiting_for_name)
    dp.register_message_handler(
        surname_writen, state=AuthenticationState.waiting_for_surname)
    dp.register_message_handler(
        patronymic_writen, state=AuthenticationState.waiting_for_patronymic)
    dp.register_message_handler(
        group_name_writen, state=AuthenticationState.waiting_for_group_name)
    dp.register_callback_query_handler(
        user_data_confirmed,
        text="confirm_user_data",
        state=AuthenticationState.waiting_for_confirmation
    )
    dp.register_callback_query_handler(
        re_enter_user_data,
        text="re_enter_user_data",
        state=AuthenticationState.waiting_for_confirmation
    )
