import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌
def fire_gun():
	# ✅ ↓ your code here ↓ ✅	
	if spin_chamber() == bullet_position:
		print("You are dead!")
	else: print("Sigue viviendo")
	return None


print(fire_gun())
