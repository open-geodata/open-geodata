"""
Convert Coordenadas

"""





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



# https://stackoverflow.com/questions/33997361/how-to-convert-degree-minute-second-to-degree-decimal

# # Degrees, minutes, seconds to Decimal degrees
# def dms2dd(degrees, minutes, seconds, direction):
#     dd = (float(degrees.replace(',', '.')) +
#           float(minutes.replace(',', '.'))/60 +
#           float(seconds.replace(',', '.'))/(60*60)
#          )
#     if direction == 'E' or direction == 'N':
#         dd *= 1

#     elif direction == 'W' or direction == 'O' or direction == 'S':
#         dd *= -1

#     return dd

# # Decimal degrees to Degrees, minutes, seconds
# def dd2dms(deg):
#     d = int(deg)
#     md = abs(deg - d) * 60
#     m = int(md)
#     sd = (md - m) * 60
#     sd = round(sd, 10)
#     return [d, m, sd]

# # Parse Values
# def parse_dms(dms):
#     coord = re.split('[^\d\w\.,]+', dms)
#     lat = dms2dd(coord[0], coord[1], coord[2], coord[3])
#     return (lat)

# # Single Value
# # DMS to DD
# coordinates_dms = '53°19\'03,208\"S'
# coordinates_dd = parse_dms(coordinates_dms)
# print('A coordenada DMS "{}" foi convertida para coordenada DD "{}"'.format(coordinates_dms, coordinates_dd))

# # DD to DMS
# d, m, s = dd2dms(coordinates_dd)
# print('A coordenada DD "{}" foi convertida em "{}", "{}" e "{}"'.format(coordinates_dd, d, m, s))





if __name__ == '__main__':
    print(dms2dd('23°06’12,48”S'))
    print(dms2dd_infoaguas('22 13 52'))
    pass


