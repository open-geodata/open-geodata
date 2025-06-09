import pprint

import geopandas as gpd
import pytesseract
from pathlib import Path
from SICAR import Polygon, Sicar, State


class SICAR:
    """
    Class to handle the Sicar data provider.
    """

    def __init__(
        self,
        tesseract_path: str | Path,
    ):
        """
        Initialize the Sicar data provider with optional parameters.
        """
        tesseract_path = Path(tesseract_path)
        if tesseract_path.is_file():
            self.tesseract_path = Path(tesseract_path)

            # Set the tesseract command path for pytesseract
            pytesseract.pytesseract.tesseract_cmd = (
                self.tesseract_path.as_posix()
            )

        else:
            raise ValueError(f"Invalid tesseract path: {tesseract_path}")

        # Create Sicar instance
        self.car = Sicar()

    @property
    def release_dates(self):
        """
        Method to retrieve data from the Sicar provider.
        """
        # Implementation for retrieving data goes here
        return self.car.get_release_dates()

    @property
    def list_states(self) -> list[State]:
        return [x for x in State]

    @property
    def list_layers(self) -> list[Polygon]:
        return [x for x in Polygon]

    def download_data(
        self, sigla_estado: State, layer: Polygon, output_path, *args, **kwargs
    ):
        """
        Download data for a specific state.
        """
        n_tentativas = kwargs.get('n_tentativas', 3)
        tentativa = 0

        while tentativa < n_tentativas:
            try:
                self.car.download_state(
                    state=sigla_estado,
                    polygon=layer,
                    folder=output_path,
                )
                print(f"Polygon for {sigla_estado} downloaded successfully.")
                break

            except Exception as e:
                print(f"Error downloading polygon for {sigla_estado}: {e}")
                tentativa += 1


if __name__ == "__main__":
    # Example usage
    # sicar = SICAR(tesseract_path="/usr/bin/tesseract")
    sicar = SICAR(
        tesseract_path=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    )
    release_dates = sicar.release_dates
    pprint.pprint(release_dates)

    #
    print(sicar.list_states)

    # Example of using the Sicar class to get a state
    # state = sicar.car.get_state(State.ACRE)
    # print(f"State: {state.name}, Code: {state.code}")
