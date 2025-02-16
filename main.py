from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDFloatingActionButton
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
import requests

KV = '''
MDBoxLayout:
    orientation: 'vertical'
    padding: 10
    spacing: 20

    MDCard:
        size_hint: (1, 0.2)
        padding: 15
        radius: 20
        md_bg_color: 0.1, 0.1, 0.1, 1  # Dark theme card
        MDTextField:
            id: ip_input
            hint_text: "Enter ESP8266 IP Address"
            text_color_focus: 1, 1, 1, 1
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.9
            mode: "rectangle"

    MDBoxLayout:
        size_hint_y: 0.4
        spacing: 10
        padding: 10
        pos_hint: {"center_x": 0.5}
        MDBoxLayout:
            size_hint: (1, 1)
            spacing: 20
            MDFloatingActionButton:
                icon: "arrow-left"
                md_bg_color: 1, 0, 0, 1
                on_press: app.send_command("/left")
            MDFloatingActionButton:
                icon: "arrow-up"
                md_bg_color: 0, 1, 0, 1
                on_press: app.send_command("/forward")
            MDFloatingActionButton:
                icon: "arrow-right"
                md_bg_color: 1, 0, 0, 1
                on_press: app.send_command("/right")

    MDBoxLayout:
        size_hint_y: 0.3
        spacing: 20
        padding: 10
        pos_hint: {"center_x": 0.5}
        MDFloatingActionButton:
            icon: "arrow-down"
            md_bg_color: 0, 0, 1, 1
            on_press: app.send_command("/backward")
        MDFloatingActionButton:
            icon: "stop"
            md_bg_color: 1, 1, 0, 1
            on_press: app.send_command("/stop")
'''

class CarControllerApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def send_command(self, command):
        esp_ip = self.root.ids.ip_input.text.strip()
        if esp_ip:
            try:
                url = f"http://{esp_ip}{command}"
                response = requests.get(url)
                print(f"Sent: {url} | Response: {response.text}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    CarControllerApp().run()
