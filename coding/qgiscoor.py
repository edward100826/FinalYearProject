layer = iface.activeLayer()
output_file = open('c:/Users/ProHacker/Downloads/usage.txt', 'w')
for f in layer.getFeatures():
    geom = f.geometry()
    line = '%s, %f, %f\n' % (f['Usage'],geom.asPoint().y(), geom.asPoint().x())
    unicode_line = line.encode('utf-8')
    output_file.write(unicode_line)
output_file.close()