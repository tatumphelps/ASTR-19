class animal: 
	def __init__(self, arm_length, leg_length, num_eyes,):
		self.arm_length = float(arm_length)
		self.leg_length = float(leg_length)
		self.num_eyes = int(num_eyes)

	def has_tail(self):
		return True

	def is_furry(self):
		return True


	def describe(self):
		polar_bear = PolarBear(arm_length = float(1.7))
		print("Polarbear arm length", arm_length)

	def describe(self):
		polar_bear = PolarBear(leg_length = float(1.7))
		print("Polarbear leg length", leg_length)

	def describe(self):
		polar_bear = PolarBear(num_eyes = int(2))
		print("Polarbear number of eyes", num_eyes)


if __name__ == "__main__":
	polar_bear = Polarbear(1.7, 1.7, 2)
	polar_bear.describe()