from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from tgbot.services.fake_db import DatabaseFaker


class DbMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self):
        super().__init__()

    async def pre_process(self, obj, data, *args):
        data["db"] = DatabaseFaker

    async def post_process(self, obj, data, *args):
        del data["db"]
