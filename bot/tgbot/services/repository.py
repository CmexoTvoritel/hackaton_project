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
