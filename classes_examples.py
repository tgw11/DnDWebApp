
class Car:

    def __init__(self, tueren: int, fenster: int):
        self.tueren = tueren
        self.fenster = fenster

    def get_tueren(self):
        return self.tueren
    

vw = Car(tueren =1, fenster =3)
print(vw.get_tueren())
print(type(vw))

