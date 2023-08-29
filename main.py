import gltf
import asyncio
import platform

from src.common_tools.path_item import PathMan
from src.decode_tools.decode_buffers import decode_buffers
from src.gltf_tools.gltf_loader import load_gltf


async def start():
    print("START")
    paths = PathMan()
    gltf_data = load_gltf(paths.input)
    gltf_model = gltf.GLTF.load(gltf_data)
    if not gltf_data:
        return
    await decode_buffers(gltf_model)


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(start())
