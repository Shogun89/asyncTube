from pytube import YouTube
import asyncio
import os


class asyncTube:

    def __init__(self, links, path=os.getcwd()):
        self.links = links
        self.path = path

    def GET(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._start(loop))

    async def _start(self, loop):
        await asyncio.wait([loop.create_task(self._fetch(vid_name, vid_link, 0)) for vid_name, vid_link in self.links.items()] if type(self.links) == dict else [loop.create_task(self._fetch(i, i, 0)) for i in self.links])

    async def _fetch(self, vidname, vidlink, count):
        print('Downloading: {}'.format(vidname))
        await asyncio.sleep(0.0001)
        if count < 3:
            try:
                YouTube(vidlink).streams.first().download(self.path)
                print('Finished Downloading: {}'.format(vidname))
            except:
                count += 1
                print('Could not download: {}, retrying {} more times'.format(vidname, 3 - count))
                await self._fetch(vidname, vidlink, count)
        else:
            print('You are out of tries for downloading: {}'.format(vidname))
