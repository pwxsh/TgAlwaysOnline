import asyncio

from tgalwaysonline.config import API_ID, API_HASH, SESSION_NAME, DELAY
from tgalwaysonline.core import TgAlwaysOnline


async def main() -> None:
	if not (API_ID and API_HASH and SESSION_NAME and DELAY):
		raise ValueError("Please enter your account data in .env.example file, then rename it to .env")

	async with TgAlwaysOnline(SESSION_NAME, API_ID, API_HASH) as tgao:
		await tgao.run(int(DELAY))


asyncio.run(main())
