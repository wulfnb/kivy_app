import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require("1.11.1")

from pages import *


class EpicApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen(name='Connect')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name='Info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)
        
        return self.screen_manager


def button_ppress(instance):
    chat_app.info_page.update_info("Button pressed")
    chat_app.screen_manager.current = 'Info'

chat_app = EpicApp()

if __name__ == "__main__":
    chat_app.run()