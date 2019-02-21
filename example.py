import asyncio
import aiohttp

from pyEstradasPT import Cameras, EstradasPT

async def main():
    async with aiohttp.ClientSession() as session:
        cameras = await Cameras.get(session)

        print("Cameras:")
        for camera in await cameras.full_list():
            print(camera)


        print("URL of camera by name (2ªCircular, km 5+700 - Telheiras):")
        url = await cameras.UrlByCameraName("2ªCircular, km 5+700 - Telheiras")
        print(url)

        print("URL of camera by ID (124600):")
        url = await cameras.UrlByCameraId(124600)
        print(url)

        print("URL of camera by ID (121696):")
        url = await cameras.UrlByCameraId(121696)
        print(url)

        print("Total # cameras:")
        count = await cameras.number_of_cameras()
        print(count)


asyncio.get_event_loop().run_until_complete(main())


