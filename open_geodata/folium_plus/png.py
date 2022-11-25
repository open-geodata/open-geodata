"""
Sobreescreve método "to_png" do folium
com objetivo de usar um webdriver que não está localizado
"""

import time

import folium
from folium.utilities import temp_html_filepath
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


class MyMap(folium.Map):
    """
    _summary_
    """

    def to_png_custom(self, gecko_path, log_path, delay=3):
        """
        Export the HTML to byte representation of a PNG image.

        Uses selenium to render the HTML and record a PNG. You may need to
        adjust the `delay` time keyword argument if maps render without data or tiles.

        Examples
        --------
        >>> m._to_png()
        >>> m._to_png(time=10)  # Wait 10 seconds between render and snapshot.
        """
        if self._png_image is None:
            options = FirefoxOptions()
            options.add_argument('--headless')

            # Adicionado por mim!
            service = FirefoxService(
                executable_path=gecko_path, log_path=log_path
            )
            driver = webdriver.Firefox(options=options, service=service)

            html = self.get_root().render()
            with temp_html_filepath(html) as fname:
                # We need the tempfile to avoid JS security issues.
                driver.get(f'file:///{fname}')
                driver.maximize_window()
                time.sleep(delay)
                png = driver.get_screenshot_as_png()
                driver.quit()
            self._png_image = png
        return self._png_image


if __name__ == '__main__':

    import io

    from paths import docs_path_imgs, scrapy_path_driver, scrapy_path_logs
    from PIL import Image

    # Cria mapa como objeto
    m = MyMap(location=[-23.9619271, -46.3427499], zoom_start=12)

    # Salva
    img_data = m.to_png_custom(
        gecko_path=scrapy_path_driver / 'geckodriver.exe',
        log_path=scrapy_path_logs / 'geckodriver.log',
        delay=7,
    )
    img = Image.open(io.BytesIO(img_data))
    img.save(docs_path_imgs / 'cetesb_enquadramento.png')
