import typing


class Repo:
    """Db abstraction layer"""

    def __init__(self, conn):
        self.conn = conn

    async def authenticate_user(self, tg_id, email, name, surname, patronymic, group_name) -> None:
        """Добавляет данные о пользователе в БД"""
        await self.conn.execute(
            "INSERT INTO users (tg_id, mail, name, surname, patronymic, group_name) VALUES ($1, $2, $3, $4, $5, $6)",
            tg_id, email, name, surname, patronymic, group_name
        )
        return

    async def check_user_is_exists(self, tg_id) -> bool:
        """Проверяет есть ли юзер в БД"""
        check = await self.conn.fetchval(
            "SELECT EXISTS(SELECT 1 FROM users WHERE tg_id=$1)",
            tg_id
        )
        return check

    async def get_users_by_group_name(self, group_name) -> typing.List[int]:
        """Возвращаеет tg_id всех юзеров переданной группы"""
        users = await self.conn.fetch(
            "SELECT tg_id FROM users WHERE group_name=$1",
            group_name
        )
        return [user[0] for user in users]

    async def get_question_ids_by_lec_id(self, lec_id) -> typing.List[int]:
        """Возвращаеет данные всех вопросов к определённой лекции"""
        q_data = await self.conn.fetch(
            "SELECT id FROM lecture_questions WHERE lecture_id=$1",
            lec_id
        )
        return [q[0] for q in q_data]

    async def get_question_data_by_q_id(self, q_id) -> typing.List[int]:
        """Возвращаеет данные всех вопросов к определённой лекции"""
        q_data = await self.conn.fetchrow(
            "SELECT q_text, answers FROM lecture_questions WHERE id=$1",
            q_id
        )
        return [q_data[0], q_data[1]]

    async def get_group_names_by_q_id(self, q_id) -> int:
        """Возвращаеет кол-во всех вопросов к определённой лекции"""
        group_names = await self.conn.fetch(
            "SELECT group_names FROM lectures WHERE id=(SELECT lecture_id FROM lecture_questions WHERE id=$1)",
            q_id
        )
        return [group_name[0][0] for group_name in group_names]

    async def get_count_questions_by_lec_id(self, lec_id) -> int:
        """Возвращаеет кол-во всех вопросов к определённой лекции"""
        count = await self.conn.fetchval(
            "SELECT COUNT(*) FROM lecture_questions WHERE lecture_id=$1",
            lec_id
        )
        return count

    async def save_student_answer(self, q_id, student_id, answer: bool) -> None:
        """Добавляет данные о пользователе в БД"""
        await self.conn.execute(
            "INSERT INTO Student_answers (q_id, student_id, answer) VALUES ($1, $2, $3)",
            q_id, student_id, answer
        )
        return
