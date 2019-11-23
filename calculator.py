# -*- coding: utf-8 -*-

from kivy.app import App


class CalculatorApp(App):
    def __init__(self, **kwargs):
        super(CalculatorApp, self).__init__(**kwargs)
        self.title = 'calculator'


if __name__ == '__main__':
    CalculatorApp().run()
