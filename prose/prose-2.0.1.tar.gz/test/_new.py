from prose import FitsManager

fm = FitsManager("/Users/lgrcia/spirit/bad_pixels_managment/Spirit_20220115_Sp0921-2104_zYJ")
print(fm)

from prose import pipeline

phot = pipeline.AperturePhotometry(fm.reduced, fm.stack)
phot.run("test.phot")