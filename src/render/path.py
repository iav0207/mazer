from os import makedirs
from os.path import join, exists


def build_output_path(file_format, file_name=None):
    out_dir = 'out'
    if not exists(out_dir):
        makedirs(out_dir)
    file_name = file_name or 'maze'
    return join(out_dir, f'{file_name}.{file_format}')
