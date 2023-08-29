import base64

from gltf import GLTF


async def decode_buffers(gltf_model: GLTF):
    buffers = gltf_model.buffers
    for buffer_idx, buffer in enumerate(buffers):
        print(f"Buffer {buffer_idx} size: {buffer.byte_length} bytes")
        buffer_data = buffer.data
        decoded_bytes = base64.b64decode(buffer_data)
        # decoded_text = decoded_bytes.decode("utf-8")
        print(buffer_data)
        print(decoded_bytes)
        # print(decoded_text)
