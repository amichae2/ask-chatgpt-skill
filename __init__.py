from mycroft import MycroftSkill, intent_file_handler


class AskChatgpt(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('chatgpt.ask.intent')
    def handle_chatgpt_ask(self, message):
        query = message.data.get('query')
        answer = ''

        self.speak_dialog('chatgpt.ask', data={
            'query': query,
            'answer': answer
        })


def create_skill():
    return AskChatgpt()

