import json
from typing import Optional


def load_gltf(gltf_path) -> Optional[dict]:
    try:
        with open(gltf_path, 'rb') as gltf_file:
            return json.load(gltf_file)
    except Exception as ex:
        print("ERROR!", ex)
