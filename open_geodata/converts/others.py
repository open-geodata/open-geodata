import re
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