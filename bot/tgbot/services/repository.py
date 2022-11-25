import typing


class Repo:
    """Db abstraction layer"""

    def __init__(self, conn):
        self.conn = conn

    async def add_user(self, user_id) -> None:
        """Store user in DB"""
        await self.conn.execute(
            "INSERT INTO Userss (user_id) VALUES ($1)",
            user_id,
        )
        return

    async def list_users(self) -> typing.List[int]:
        """List all bot users"""
        users = await self.conn.fetch(
            "SELECT user_id FROM Userss"
        )
        return [user[0] for user in users]
