from PIL import Image
import os
import shutil

class FileManager:
	filename = None
	level = None

	# Initialization func

	def __init__(self, filename, level):
		if level > 0 and level < 6:
			self.filename = str(filename)
			self.level = int(level)
		else:
			print("Invalid access level! Allowed only 1-6 access levels")

	# Funcs for work with text files(.txt)

	# Read line in text file

	def readline(self):
		if self.level >= 1:
			try:
				with open(f"{self.filename}", "r") as f:
					raw = f.readline()
				return raw
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 1")

	# Read lines in text file (as array)

	def readlines(self):
		if self.level >= 1:
			try:
				with open(f"{self.filename}", "r") as f:
					raw = f.readlines()
				return raw
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 1")

	# Set content in text file

	def set(self, text):
		if self.level >= 3:
			try:
				with open(f"{self.filename}", "w") as f:
					f.write(text)
					return 1
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 3")

	# Add content in text file with separator(default separator is empty)

	def add(self, text, sep=""):
		if self.level >= 2:
			try:
				with open(f"{self.filename}", "r") as f:
					old = f.read()
				with open(f"{self.filename}", "w") as f:
					f.write(old + sep + text)
					return 1
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 2")

	# Replace certain content in text file

	def replace(self, _from, _to):
		if self.level >= 3:
			try:
				with open(f"{self.filename}", "r") as f:
					data = f.read().replace(_from, _to)
				with open(f"{self.filename}", "w") as f:
					f.write(data)
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 3")

	# Funcs for general work with files

	# Rename file(from self.filename to name)

	def rename(self, name):
		if self.level >= 4:
			try:
				os.rename(f"{self.filename}", name)
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 4")

	# Delete file

	def delete(self):
		if self.level == 5:
			try:
				os.remove(f"{self.filename}")
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 5")

	# Copy file

	def copy(self, dst):
		if self.level >= 4:
			try:
				shutil.copy2(f"{self.filename}", f"{dst}")
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 4")

	# Move file

	def move(self, dst):
		if self.level >= 4:
			try:
				shutil.move(f"{self.filename}", f"{dst}")
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 4")

class FilesManager:
	level = None

	# Initalization func

	def __init__(self, level):
		if level > 0 and level < 6:
			self.level = int(level)
		else:
			print("Invalid access level! Allowed only 1-6 access levels")

	# Funcs for work with text files(.txt)

	# Read line in text file

	def readline(self, dst):
		if self.level >= 1:
			try:
				with open(f"{dst}", "r") as f:
					raw = f.readline()
				return raw
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 1")

	# Read lines in text file (as array)

	def readlines(self, dst):
		if self.level >= 1:
			try:
				with open(f"{dst}", "r") as f:
					raw = f.readlines()
				return raw
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 1")

	# Set content in text file

	def set(self, dst, text):
		if self.level >= 3:
			try:
				with open(f"{dst}", "w") as f:
					f.write(text)
					return 1
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 3")

	# Add content in text file with separator(default separator is empty)

	def add(self, dst, text, sep=""):
		if self.level >= 2:
			try:
				with open(f"{dst}", "r") as f:
					old = f.read()
				with open(f"{dst}", "w") as f:
					f.write(old + sep + text)
					return 1
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 2")

	# Replace certain content in text file

	def replace(self, dst, _from, _to):
		if self.level >= 3:
			try:
				with open(f"{dst}", "r") as f:
					data = f.read().replace(_from, _to)
				with open(f"{dst}", "w") as f:
					f.write(data)
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 3")

	# Funcs for general work with files

	# Create line

	def create(self, dst):
		if self.level >= 2:
			f = open(f"{dst}", "a")
			f.close()
		else:
			print(f"Low access level! {self.level}, but need 2")

	# Rename file(from self.filename to name)

	def rename(self, dst, name):
		if self.level >= 4:
			try:
				os.rename(f"{dst}", name)
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 4")

	# Delete file

	def delete(self, dst):
		if self.level == 5:
			try:
				os.remove(f"{dst}")
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 5")

	# Copy file

	def copy(self, dst, new_dst):
		if self.level >= 4:
			try:
				shutil.copy2(f"{dst}", f"{new_dst}")
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 4")

	# Move file

	def move(self, dst, new_dst):
		if self.level >= 4:
			try:
				shutil.move(f"{dst}", f"{new_dst}")
			except FileNotFoundError:
				print("Something went wrong...")
		else:
			print(f"Low access level! {self.level}, but need 4")