import asyncio
import time

import requests


async def counter(until: int = 10) -> None:
    now = time.perf_counter()
    print("Started counter")
    for i in range(until):
        last = now
        await asyncio.sleep(0.01)
        now = time.perf_counter()
        print(f"{i}: Was asleep for {now - last}s")


def send_request(url: str) -> int:
    print("Sending HTTP request")
    response = requests.get(url)
    return response.status_code


# creates a separate thread to run that particular blocking task (send request)
async def send_async_request(url: str) -> int:
    return await asyncio.to_thread(send_request, url)


async def main() -> None:
    status_code, _ = await asyncio.gather(
        send_async_request("https://www.arjancodes.com"), counter()
    )

    # task = asyncio.create_task(counter())
    # status_code = await send_async_request("https://www.arjancodes.com")
    print(f"Got HTTP response with status {status_code}")

    # await task


asyncio.run(main())
