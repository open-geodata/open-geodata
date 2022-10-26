"""
Convert Coordenadas

"""


def dms2dd_daee(coord):
    """
    Convert geographic coordinates in
    format degrees, minutes and seconds (22° 55' 09'')
    in decimal degrees (e.g. -22.91916666666667)

    Estilo DAEE Hidrologia

    :param coord: string 23° 06' 09''
    :return: float -22.91916666666667
    """
    # Splitar coordenada
    coord = coord.replace("''", '')
    coord = coord.replace("'", '-')
    coord = coord.replace("°", '-')
    coord = coord.replace(' ', '')
    coord = coord.split('-')
    graus = float(coord[0])
    minutos = float(coord[1])
    segundos = float(coord[2])

    # Calcular
    coord_dm = graus + (minutos / 60) + (segundos / 3600)

    # Converter parâmetro textual
    return coord_dm * -1


def dms2dd(coord):
    """
    Convert geographic coordinates in
    format degrees, minutes and seconds (23°06’12,48”S)
    in decimal degrees (e.g. -23.10346666666667)

    Estilo Informações Técnicas CETESB

    :param coord: string 23°06’12,48”S
    :return: float -23.10346666666667
    """
    # Splitar coordenada
    graus = float(coord.split('°')[0])
    minutos = float((coord.split('°')[1]).split('’')[0])
    segundos = float(
        (((coord.split('°')[1]).split('’')[1]).split('”')[0]).replace(',', '.'))
    direction = (((coord.split('°')[1]).split('’')[1]).split('”')[1])

    # Calcular
    coord_dm = graus + (minutos / 60) + (segundos / 3600)

    # Converter parâmetro textual
    if direction in ('S', 's', 'O', 'o'):
        return coord_dm * -1
    else:
        return coord_dm


def dms2dd_infoaguas(coord_dms):
    """
    Para usar em uma coluna
    df.loc[:, 'latitude_dd'] = df['latitude_dms'].astype(str).apply(lambda x: dms2dd(x))

    :param coord_dms:
    :return:
    """
    coord_dms = coord_dms.strip()
    try:
        coord_deg = float(coord_dms.split(' ', maxsplit=2)[0])
        coord_min = float(coord_dms.split(' ', maxsplit=2)[1])
        coord_sec = float(coord_dms.split(' ', maxsplit=2)[2])
        coord_dd = coord_deg + (coord_min / 60) + (coord_sec / 3600)
        coord_dd = coord_dd * -1
    except:
        coord_dd = 0
    return coord_dd


if __name__ == '__main__':
    print(dms2dd('23°06’12,48”S'))
    print(dms2dd_infoaguas('22 13 52'))
    print(dms2dd_daee("22° 55' 09''"))
