from mycroft import MycroftSkill, intent_file_handler


class Todolist(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('todolist.intent')
    def handle_todolist(self, message):
        self.speak_dialog('todolist')


def create_skill():
    return Todolist()

