import transistordatabase as tdb

tdb.print_tdb()

t1 = tdb.load("Fuji_2MBI300XBE065-50")
t2 = tdb.load("CREE_WAB300M12BM3")
t3 = tdb.load("Infineon_IPW65R090CFD7")

#t1.export_datasheet()
#t2.export_datasheet()
t3.export_datasheet()