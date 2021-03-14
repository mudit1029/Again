class flight():
	def __init__(self, capacity):
		self.capacity = capacity
		self.passengers = []

	def add_passenger(self , name):
		if not self.open_seats():
			return False
		self.passengers.append(name)
		return True

	def open_seats(self):
		return self.capacity - len(self.passengers)	
		
Flight = flight(3)	

people = ["Mudit", "Anurag", "Muskan", "Adab"]

for person in people:
	success = Flight.add_passenger(person)
	if success:
		print(f"{person} added succesfully to the flight.")	
	else :
		print(f"Not enough capacity for {person}.")	