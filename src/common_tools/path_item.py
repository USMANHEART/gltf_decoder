from os.path import join
from src.common_tools.constants import PROJECT_DIR


class PathMan:
    def __init__(self):
        self.projDir = join(PROJECT_DIR)
        self.input = join(self.projDir, "..", "test.gltf")
