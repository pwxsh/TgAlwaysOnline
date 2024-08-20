import asyncio
from datetime import datetime
from typing import Optional, Union

from pyrogram.client import Client
from pyrogram.raw.functions.account.update_status import UpdateStatus


class TgAlwaysOnline:
	def __init__(
		self,
		session_name: str,
		api_id: Union[int, str],
		api_hash: str
	):
		self._client = Client(session_name, api_id, api_hash)
		self._is_running = False

	async def _stay_online_loop(self, delay: int) -> None:
		print(f"[{datetime.now()}]: Started online status updating with a {delay}s delay")

		while self._is_running:
			result = await self._client.invoke(
				UpdateStatus(offline=False)
			)

			print(f"[{datetime.now()}]: Online status {'updated' if result else 'is already online'}")
			await asyncio.sleep(delay)

	async def run(self, delay: int) -> None:
		if not self._is_running:
			self._is_running = True
			await self._client.start()
			await self._stay_online_loop(delay)
		else:
			print("[{datetime.now()}]: Online status updating is already running")

	async def stop(self) -> None:
		if not self._is_running:
			self._is_running = False
			await self._client.stop()
			print("[{datetime.now()}]: Online status updating stopped")

	async def __aenter__(self) -> "TgAlwaysOnline":
		return self

	async def __aexit__(self, *exc) -> None:
		await self.stop()
