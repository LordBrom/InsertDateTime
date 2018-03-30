import sublime
import sublime_plugin
from datetime import datetime

class InsertDateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		date = datetime.now().date()
		for sel in self.view.sel():
			self.view.replace(edit,
				              sel,
			             	  date.strftime("%m/%d/%y"))

class InsertTimeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		time = datetime.now().time()
		for sel in self.view.sel():
			self.view.replace(edit,
				             sel,
				             time.strftime("%H:%M"))
