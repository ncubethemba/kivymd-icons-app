from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix. recycleview import RecycleView
from kivy.properties import StringProperty
from kivymd.icon_definitions import md_icons
from kivymd.uix.card import MDCard
from kivy.uix.gridlayout import GridLayout

class MainInterface(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def search(self):
        self.ids.recycleview.data=[{'icon_to_display': str(i) } for i in md_icons.keys() if self.ids.textfield.text in i]
class CustomRecycleView(RecycleView):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.data=[{'icon_to_display': str(i) }  for i in md_icons.keys()]
        
class CustomGrid(GridLayout):
    pass
class ElementCard(MDCard):
    icon_to_display=StringProperty()
class MainApp(MDApp):
    pass
MainApp().run()
  