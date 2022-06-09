# Makefile for firefly project
# Author: Stanislav Gabriš 	(xgabri18@stud.fit.vutbr.cz)
# Author: Adam Fabo 		(xfaboa00@stud.fit.vutbr.cz)
EXE = fireflies
TARNAME=09_xfaboa00_xgabri18
FILES= Makefile dokumentace.pdf README.md fireflies.h fireflies.cpp fireflies_main.cpp

all: clean fireflies

fireflies: fireflies.o
	g++ -o fireflies fireflies.o fireflies_main.o

fireflies.o:
	g++ -c fireflies_main.cpp fireflies.cpp

tar:
	tar -czvf $(TARNAME).tar.gz $(FILES)


clean:
	rm -f *.o $(EXE)



#all: fireflies_backup.cpp
#	g++ -o fireflies_backup fireflies_backup.cpp

