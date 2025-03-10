from PIL import Image
import os
import shutil

class FileManager:
	filename = None
	level = None
	encoding = None

	# Initialization func

	def __init__(self, filename: str, level: int, encoding: str = "UTF-8"):
		if 0 < level < 6:
			self.filename = filename
			self.level = level
			self.encoding = encoding
		else:
			print("Invalid access level! Allowed only 1-6 access levels")

	# Funcs for work with text files(.txt)

	# Read line in text file

	def readline(self):
		if self.level >= 1:
			try:
				with open(f"{self.filename}", "r", encoding=self.encoding) as f:
					raw = f.readline()
				return raw
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 1"

	# Read lines in text file (as array)

	def readlines(self):
		if self.level >= 1:
			try:
				with open(f"{self.filename}", "r", encoding=self.encoding) as f:
					raw = f.readlines()
				return raw
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 1"

	# Set content in text file

	def set(self, text):
		if self.level >= 3:
			try:
				with open(f"{self.filename}", "w", encoding=self.encoding) as f:
					f.write(text)
					return 1
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 3"

	# Add content in text file with separator(default separator is empty)

	def add(self, text, sep=""):
		if self.level >= 2:
			try:
				with open(f"{self.filename}", "r", encoding=self.encoding) as f:
					old = f.read()
				with open(f"{self.filename}", "w", encoding=self.encoding) as f:
					f.write(old + sep + text)
					return 1
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 2"

	# Replace certain content in text file

	def replace(self, _from, _to):
		if self.level >= 3:
			try:
				with open(f"{self.filename}", "r", encoding=self.encoding) as f:
					data = f.read().replace(_from, _to)
				with open(f"{self.filename}", "w", encoding=self.encoding) as f:
					f.write(data)
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 3"

	# Funcs for general work with files

	# Rename file(from self.filename to name)

	def rename(self, name):
		if self.level >= 4:
			try:
				os.rename(f"{self.filename}", name)
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 4"

	# Delete file

	def delete(self):
		if self.level == 5:
			try:
				os.remove(f"{self.filename}")
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 5"

	# Copy file

	def copy(self, dst):
		if self.level >= 4:
			try:
				shutil.copy2(f"{self.filename}", f"{dst}")
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 4"

	# Move file

	def move(self, dst):
		if self.level >= 4:
			try:
				shutil.move(f"{self.filename}", f"{dst}")
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 4"

class FilesManager:
	level = None
	_dir = None

	# Initalization func

	def __init__(self, level):
		if 0 < level < 6:
			self.level = int(level)
		else:
			print("Invalid access level! Allowed only 1-6 access levels")

	# Funcs for work with text files(.txt)

	# Read line in text file

	def readline(self, dst, use_wd=False, encoding: str = "UTF-8"):
		if self.level >= 1:
			try:
				if use_wd == True and "/" in self._dir:
					with open(f"{self._dir}{dst}", "r", encoding=encoding) as f:
						raw = f.readline()
				else:
					with open(f"{dst}", "r", encoding=encoding) as f:
						raw = f.readline()
				return raw
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 1"

	# Read lines in text file (as array)

	def readlines(self, dst, use_wd=False, encoding: str = "UTF-8"):
		if self.level >= 1:
			try:
				if use_wd == True and "/" in self._dir:
					with open(f"{self._dir}{dst}", "r", encoding=encoding) as f:
						raw = f.readlines()
				else:
					with open(f"{dst}", "r", encoding=encoding) as f:
						raw = f.readlines()
				return raw
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 1"

	# Set content in text file

	def set(self, dst, text, use_wd=False, encoding: str = "UTF-8"):
		if self.level >= 3:
			try:
				if use_wd == True and "/" in self._dir:
					with open(f"{self._dir}{dst}", "w", encoding=encoding) as f:
						f.write(text)
						return 1
				else:
					with open(f"{dst}", "w", encoding=encoding) as f:
						f.write(text)
						return 1
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 3"

	# Add content in text file with separator(default separator is empty)

	def add(self, dst, text, sep="", use_wd=False, encoding: str = "UTF-8"):
		if self.level >= 2:
			try:
				if use_wd == True and "/" in self._dir:
					with open(f"{self._dir}{dst}", "r", encoding=encoding) as f:
						old = f.read()
					with open(f"{self._dir}{dst}", "w", encoding=encoding) as f:
						f.write(old + sep + text)
						return 1
				else:
					with open(f"{dst}", "r", encoding=encoding) as f:
						old = f.read()
					with open(f"{dst}", "w", encoding=encoding) as f:
						f.write(old + sep + text)
						return 1
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 2"

	# Replace certain content in text file

	def replace(self, dst, _from, _to, use_wd=False, encoding: str = "UTF-8"):
		if self.level >= 3:
			try:
				if use_wd == True and "/" in self._dir:
					with open(f"{dst}", "r", encoding=encoding) as f:
						data = f.read().replace(_from, _to)
					with open(f"{dst}", "w", encoding=encoding) as f:
						f.write(data)
				else:
					with open(f"{dst}", "r", encoding=encoding) as f:
						data = f.read().replace(_from, _to)
					with open(f"{dst}", "w", encoding=encoding) as f:
						f.write(data)
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 3"

	# Funcs for general work with files

	# Create line

	def create(self, dst, use_wd=False):
		if self.level >= 2:
			if use_wd == True and "/" in self._dir:
				f = open(f"{self._dir}{dst}", "w")
			else:
				f = open(f"{dst}", "w")
			f.close()
		else:
			return f"Low access level! {self.level}, but need 2"

	# Rename file(from self.filename to name)

	def rename(self, dst, name, use_wd=False):
		if self.level >= 4:
			try:
				if use_wd == True and "/" in self._dir:
					os.rename(f"{self._dir}{dst}")
				else:
					os.rename(f"{dst}", name)
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 4"

	# Delete file

	def delete(self, dst, use_wd=False):
		if self.level == 5:
			try:
				if use_wd == True and "/" in self._dir:
					os.remove(f"{self._dir}{dst}")
				else:
					os.remove(f"{dst}")
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 5"

	# Copy file

	def copy(self, dst, new_dst, use_wd=False):
		if self.level >= 4:
			try:
				if use_wd == True and "/" in self._dir:
					shutil.copy2(f"{self._dir}{dst}", f"{new_dst}")
				else:
					shutil.copy2(f"{dst}", f"{new_dst}")
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 4"

	# Move file

	def move(self, dst, new_dst, use_wd=False):
		if self.level >= 4:
			try:
				if use_wd == True and "/" in self._dir:
					shutil.move(f"{self._dir}{dst}")
				else:
					shutil.move(f"{dst}", f"{new_dst}")
			except FileNotFoundError:
				return "Something went wrong..."
		else:
			return f"Low access level! {self.level}, but need 4"

	# Set work directory (cd)

	def cd(self, _dir):
		if "/" in _dir:
			self._dir = _dir
		else:
			return "Error! It's not directory!"
