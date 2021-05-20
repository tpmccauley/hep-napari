import click
import logging
import napari

import numpy as np

logging.basicConfig(level=logging.INFO)

@click.command()
@click.argument('input_file_name')
def hep_napari(
        input_file_name: str,
) -> None:
    '''
    Args:
       input_file_name: name of the input ROOT file
    '''
    logging.info(f'Opening {input_file_name}')

    with napari.gui_qt():

        napari_viewer = napari.Viewer()


if __name__ == '__main__':
    hep_napari() # pylint: disable=no-value-for-parameter
