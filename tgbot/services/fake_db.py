import json
import os
from pathlib import Path

ABS_PATH = Path().resolve()


class DatabaseFaker:
    @staticmethod
    def get_data() -> dict:
        with open(
            os.path.join(ABS_PATH, "tgbot/services/Resources/data.json"), "r"
        ) as f:
            return json.load(f)
