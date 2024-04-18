"""
Opgave "Tom the Turtle":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Funktionen "demo" introducerer dig til alle de kommandoer, du skal bruge for at interagere med Tom i de følgende øvelser.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for turtle graphics:
    https://docs.python.org/3.3/library/turtle.html

Del 1:
    Skriv en funktion "square", som accepterer en parameter "length".
    Hvis denne funktion kaldes, får skildpadden til at tegne en firkant med en sidelængde på "længde" pixels.

Del 2:
     Færdiggør funktionen "visible", som skal returnere en boolsk værdi,
     der angiver, om skildpadden befinder sig i det synlige område af skærmen.
     Brug denne funktion i de følgende dele af denne øvelse
     til at få skildpadden tilbage til skærmen, når den er vandret væk.

Del 3:
    Skriv en funktion "many_squares" med en for-loop, som kalder square gentagne gange.
    Brug denne funktion til at tegne flere firkanter af forskellig størrelse i forskellige positioner.
    Funktionen skal have nogle parametre. F.eks:
        antal: hvor mange firkanter skal der tegnes?
        størrelse: hvor store er firkanterne?
        afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?

Del 4:
    Skriv en funktion, der producerer mønstre, der ligner dette:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Del 5:
    Skriv en funktion, der producerer mønstre svarende til dette:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    Funktionen skal have en parameter, som påvirker mønsterets form.

Del 6:
    Opret din egen funktion, der producerer et sejt mønster.
    Senere, hvis du har lyst, kan du præsentere dit mønster på storskærmen for de andre.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.

tom = turtle.Turtle()
tom.speed(1)
print(type(tom))

# Del 2 svar

def visible(inscreen):
    print("checking visible")
    if tom.position()[0] > 380 or tom.position()[1] > 380:
        print("Out of x bounds")
        return False
    elif tom.position()[0] < -380 or tom.position()[1] < -380:
        print("Out of y bounds")
        return False
    else:
        print("Within bounds")
        return True


    # returns true if both the x- and y-value of the turtle's position are between -480 and 480
    # you will need this: x-value: turtle_name.position()[0]
    # and this:           y-value: turtle_name.position()[1]
    return 0


# Del 1 svar
def square(lenght):
    turncount = 0
    tom.speed(1)
    while turncount < 4:
        tom.forward(lenght)
        tom.left(90)
        turncount += 1


    print("Now at " + str(tom.position()))
    visible
    print("Check")

    if visible(True)==True:
        print("True")
        return
    elif visible(False)==False:
        print("False")
        while visible(False)==False:
            tom.back(1)

    else:
        print("Nothing")
        print(visible(True))

#square(300)

# Del 3 svar
def many_squares(amount, size, distance):
    count = 1
    square(size)
    while count < amount:
        tom.forward(distance)
        square(size)
        count += 1
    print("done")

# Run many_squares(amount, size, distance) for at se svar resultatet.


# Del 4 svar

def pattern1(lenght, boxes):
    clenght = lenght
    boxesleft = boxes
    while boxesleft > 0:
        tom.forward(clenght)
        tom.left(90)
        tom.forward(clenght)
        tom.left(90)
        clenght -= lenght/boxes
        boxesleft -= 1

#Run pattern1(lenght, boxes) for at see svaret
#lenght = størrelse, boxes = antal boxe i mønsteret

# del 5

def pattern2(lenght, points):
    turns = points

    while turns > 0:
        tom.forward(lenght)
        tom.left(360-(360/points*2)/2)
        turns -= 1

pattern2(100,5)

#