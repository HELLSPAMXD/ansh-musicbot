from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from Romeo import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ Ʌɖɖ ɱ𝐞 Ʈ𝐨 yøu𝐫 𝐆ɽɵup ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ɧeɬp C𝐨ɱɱaŋɖs",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="Seʈʈɨŋɠs", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💬 𝐒uppɵɽʈ", url=f"{config.SUPPORT_GROUP}"),
            InlineKeyboardButton(
                text="𝐔pɖɑʈes 📡", url=f"{config.SUPPORT_CHANNEL}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ Ʌɖɖ ɱ𝐞 Ʈ𝐨 yøu𝐫 𝐆ɽɵup ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ɧeɬp C𝐨ɱɱaŋɖs", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="💬 𝐒uppɵɽʈ", url=f"{config.SUPPORT_GROUP}"),
            InlineKeyboardButton(
                text="𝐔pɖɑʈes 📡", url=f"{config.SUPPORT_CHANNEL}"
            )
        ],
     ]
    return buttons
