from SimpleCV import ImageSet
set = ImageSet(".")
for img in set:
oldname = img.filename
newname = oldname[0:-3] + 'jpg'
print "Converting " + oldname + " to " + newname
img.save(newname)
