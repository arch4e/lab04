import bpy
import requests

from .register import registerdcr

@registerdcr
class PostMessageToAi(bpy.types.Operator):
    bl_idname = "lab04.post_message_to_ai"
    bl_label  = "Post Message to AI"

    def execute(self, context):
        try:
            chatgpt = ChatGPT()
            messages = chatgpt.post_message()

            for msg in messages:
                if "bpy" in msg:
                    run_script(msg)

            return {'FINISHED'}
        except Exception as e:
            print(e)
            return { "CANCELLED" }

class ChatGPT():
    def __init__(self):
        self.uri = "https://api.openai.com/v1/chat/completions"

    def post_message(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + bpy.context.scene.lab04_ai.api_key
        }

        json_data = {
            'model': 'gpt-3.5-turbo',
            'messages': [
                {
                    'role': 'user',
                    'content': self.wrap_prompt()
                }
            ],
            'temperature': 0.7
        }

        response = requests.post(self.uri, headers=headers, json=json_data)
        res_json = response.json()
        messages = [x["message"]["content"] for x in res_json["choices"]]

        return messages

    def wrap_prompt(self):
        message = "Create script for Blender." \
                  + f" My Blender version is {bpy.app.version}." \
                  + " " \
                  + bpy.context.scene.lab04_ai.prompt \
                  + " Don't include any note for explanation in the response." \
                  + " I only need the code body."

        return message

def run_script(script):
    for line in script.split("\n"):
        exec(line)
