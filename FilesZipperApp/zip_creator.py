import pathlib
import zipfile

ARCHIVE_DEFAULT_NAME = "compressed.zip"

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, ARCHIVE_DEFAULT_NAME)
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)