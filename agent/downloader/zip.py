import zipfile
from pathlib import Path
import tempfile

from agent.network import RequestContent
from agent.config import IMAGE_DL_PATH


class CompressedDownloader:
    def __init__(self):
        pass

    @staticmethod
    async def download_file(url: str):
        async with RequestContent() as request:
            content = await request.get(url)
        return content

    @staticmethod
    def extract_zip(file_path: Path, extract_dir: Path):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

    async def download_and_extract(self, url: str):
        content = await self.download_file(url)
        with tempfile.NamedTemporaryFile() as tmp_file:
            tmp_file_path = Path(tmp_file.name)
            tmp_file.write(content)
            tmp_file.flush()

        extract_dir = IMAGE_DL_PATH / tmp_file_path.stem

        self.extract_zip(tmp_file_path, extract_dir)



