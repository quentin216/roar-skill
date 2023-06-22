from mycroft import MycroftSkill, intent_file_handler


class Roar(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('roar.intent')
    def handle_roar(self, message):
        self.speak_dialog('roar')


def create_skill():
    return Roar()

