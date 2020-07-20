segmentos = str(input()).split()
segmentoa = float(segmentos[0])
segmentob = float(segmentos[1])
segmentoc = float(segmentos[2])
if segmentoa < segmentob + segmentoc and segmentob < segmentoc + segmentoa and segmentoc < segmentob + segmentoa:
    perimetro = segmentoa + segmentob + segmentoc
    print('Perimetro = {:.1f}'.format(perimetro))
else:
    area = ((segmentoa + segmentob) / 2) * segmentoc
    print('Area = {:.1f}'.format(area))