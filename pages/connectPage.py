from .alpha import *

class ConnectPage(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='IP'))
        self.ip = TextInput(multiline=False)
        self.add_widget(self.ip)

        self.add_widget(Label(text='PORT'))
        self.port = TextInput(multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text='Username'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.join = Button(text='Join')
        self.join.bind(on_press=button_ppress)
        self.add_widget(Label())
        self.add_widget(self.join)
    
    def join_button(self, instance):
        
        chat_app.info_page.update_info("Button pressed")
        chat_app.screen_manager.current = 'Info'
        print("Btton pressed",self.username.text)