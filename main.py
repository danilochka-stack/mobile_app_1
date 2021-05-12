import kivy
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.properties import ObjectProperty

Config.set('graphics', 'resizable', 1)

class MainWindow(Screen):
	pass

class FunctionAim(Screen):
	pass

class Recomendation1(Screen):
	pass

class Recomendation2(Screen):
	pass

class Recomendation3(Screen):
	pass

class Recomendation4(Screen):
	pass

class Recomendation5(Screen):
	pass

class Raschet(Screen):
	summa = ObjectProperty()
	percent1 =  ObjectProperty()
	percent2 =  ObjectProperty()
	percent3 =  ObjectProperty()
	percent4 =  ObjectProperty()
	percent5 =  ObjectProperty()
	label_widget1 = ObjectProperty()
	label_widget2 = ObjectProperty()
	label_widget3 = ObjectProperty()
	label_widget4 = ObjectProperty()
	label_widget5 = ObjectProperty()
	labelpercent = ObjectProperty()
	labelryb = ObjectProperty()
	def doxod_ryb(self):
		self.colvo = 5
		try:
			self.doxodryb = int(self.summa.text)
		except ValueError:
			self.labelryb.text = ""
		try:
			self.per1 = int(self.percent1.text)
		except ValueError:
			self.label_widget1.text = ""
			self.colvo = self.colvo - 1
			self.per1 = 0
		try:
			self.per2 = int(self.percent2.text)
		except ValueError:
			self.label_widget2.text = ""
			self.colvo = self.colvo - 1
			self.per2 = 0
		try: 
			self.per3 = int(self.percent3.text)
		except ValueError:
			self.label_widget3.text = ""
			self.colvo = self.colvo - 1
			self.per3 = 0
		try: 
			self.per4 = int(self.percent4.text)
		except ValueError:
			self.label_widget4.text = ""
			self.colvo = self.colvo - 1
			self.per4 = 0
		try:
			self.per5 = int(self.percent5.text)
		except ValueError:
			self.label_widget5.text = ""
			self.colvo = self.colvo - 1
			self.per5 = 0
		try: 
			self.doxod = (self.doxodryb/self.colvo) * (float(self.per1)/100)+(self.doxodryb/self.colvo) * (float(self.per2)/100)+(self.doxodryb/self.colvo) * (float(self.per3)/100)+(self.doxodryb/self.colvo) * (float(self.per4)/100)+(self.doxodryb/self.colvo) * (float(self.per5)/100)
			self.labelryb.text = str(self.doxod)
		except ZeroDivisionError:
			self.labelryb.text = '0'


	def doxod_percent1(self):
		self.colvo = 5
		try:
			self.per1 = int(self.percent1.text)
		except ValueError:
			self.label_widget1.text = ""
			self.colvo = self.colvo - 1
			self.per1 = 0
		try:
			self.per2 = int(self.percent2.text)
		except ValueError:
			self.label_widget2.text = ""
			self.colvo = self.colvo - 1
			self.per2 = 0
		try: 
			self.per3 = int(self.percent3.text)
		except ValueError:
			self.label_widget3.text = ""
			self.colvo = self.colvo - 1
			self.per3 = 0
		try: 
			self.per4 = int(self.percent4.text)
		except ValueError:
			self.label_widget4.text = ""
			self.colvo = self.colvo - 1
			self.per4 = 0
		try:
			self.per5 = int(self.percent5.text)
		except ValueError:
			self.label_widget5.text = ""
			self.colvo = self.colvo - 1
			self.per5 = 0
		try: 
			self.doxod = (self.per1 + self.per2 + self.per3 + self.per4 + self.per5) / self.colvo
			self.labelpercent.text = str(str(self.doxod) + '%')
		except ZeroDivisionError:
			self.labelpercent.text = '0'


		
	def risk(self):
		try:
			self.per1 = int(self.percent1.text)
			if 0 <= int(self.per1) < 10:
				self.label_widget1.text = "Низкий"
				print(int(self.per1))
			elif 10 < int(self.per1) < 30:
				self.label_widget1.text = 'Средний'
			elif 30 < int(self.per1) < 50:
				self.label_widget1.text = 'Выше среднего'
			elif 50 < int(self.per1) < 80:
				self.label_widget1.text = 'Высоий'
			else:
				self.label_widget1.text = 'Максимальный'
		except ValueError:
			self.label_widget1.text = ""
		try:
			self.per2 = int(self.percent2.text)
			if 0 <=  int(self.per2) < 10:
				self.label_widget2.text = 'Низкий'
			elif 10 < int(self.per2) < 30:
				self.label_widget2.text = 'Средний'
			elif 30 < int(self.per2) < 50:
				self.label_widget2.text = 'Выше среднего'
			elif 50 <int(self.per2) < 80:
				self.label_widget2.text = 'Высокий'
			else:
				self.label_widget2.text = 'Максимальный'
		except ValueError:
			self.label_widget2.text = ""
		try: 
			self.per3 = int(self.percent3.text)
			if 0 <= int(self.per3) < 10:
				self.label_widget3.text = 'Низкий'
			elif 10 < int(self.per3) < 30:
				self.label_widget3.text = 'Средний'
			elif 30 < int(self.per3) < 50:
				self.label_widget3.text = 'Выше среднего'
			elif 50 < int(self.per3) < 80:
				self.label_widget3.text = 'Высокий'
			else:
				self.label_widget3.text = 'Максимальный'
		except ValueError:
			self.label_widget3.text = ""
		try: 
			self.per4 = int(self.percent4.text)
			if 0 <= int(self.per4) < 10:
				self.label_widget4.text = 'Низкий'
			elif 10 < int(self.per4) < 30:
				self.label_widget4.text = 'Средний'
			elif 30 < int(self.per4) < 50:
				self.label_widget4.text = 'Выше среднего'
			elif 50 < int(self.per4) < 80:
				self.label_widget4.text = 'Высокий'
			else:
				self.label_widget4.text = 'Максимальный'
		except ValueError:
			self.label_widget4.text = ""
		try:
			self.per5 = int(self.percent5.text)
			if 0 <= int(self.per5) < 10:
				self.label_widget5.text = 'Низкий'
			elif 10 < int(self.per5) < 30:
				self.label_widget5.text = 'Средний'
			elif 30 < int(self.per5) < 50:
				self.label_widget5.text = 'Выше среднего'
			elif 50 < int(self.per5) < 80:
				self.label_widget5.text = 'Высокий'
			else:
				self.label_widget5.text = 'Максимальный'
		except ValueError:
			self.label_widget5.text = ""
		

class Finansculc(GridLayout, Screen):
	def calculate(self, calculation):
		if calculation:
			try:
				self.display.text = str(eval(calculation))
			except Exception:
				self.display.text = "Error"

class DifPerCent(Screen):
	def difpercent(self):
		try:
			self.startvklad = int(self.startvklad1.text)
			self.period = int(self.period1.text)
			self.stavka = int(self.stavka1.text)
			self.sumvkladprost = int(self.startvklad) * (1 + (int(self.period) * int(self.stavka)) / (12 * 100))
			self.percent = int(self.sumvkladprost) - int(self.startvklad)
			self.sumvkladhard = int(self.startvklad) * ((1 + (int(self.stavka) / (12 * 100))) ** int(self.period))
			self.percenthard = int(self.sumvkladhard) - int(self.startvklad)
			self.easy1.text = str(self.sumvkladprost)
			self.easy2.text = str(self.percent)
			self.hard1.text = str(self.sumvkladhard)
			self.hard2.text = str(self.percenthard)
		except ValueError:
			self.easy1.text = ''
			self.easy2.text = ''
			self.hard1.text = ""
			self.hard2.text = ''



class WindowManager(ScreenManager):
	pass 

kv = Builder.load_file("my.kv")	

class MyApp(App):
	def build(self):
		return kv

if __name__ == "__main__":
	MyApp().run()
