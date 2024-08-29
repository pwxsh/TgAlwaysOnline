import asyncio

from pyrogram.client import Client
from pyrogram.raw.functions.account.update_status import UpdateStatus

from tgalwaysonline.config import API_ID, API_HASH, DELAY, PHONE_NUMBER


client = Client("TgAlwaysOnline", API_ID, API_HASH, phone_number=PHONE_NUMBER)

async def main() -> None:
	while True:
		await client.invoke(
			UpdateStatus(offline=False)
		)

		await asyncio.sleep(DELAY)


client.run(main())
