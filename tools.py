import datetime
import ollama


class Tools:

    def execute(self, action):

        tool = action["tool"]

        if tool == "time":

            return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        elif tool == "calculator":

            try:
                return str(eval(action["expression"]))
            except:
                return "Invalid expression."

        elif tool == "chat":

            response = ollama.chat(
                model="llama3",
                messages=[
                    {
                        "role": "user",
                        "content": action["query"]
                    }
                ]
            )

            return response["message"]["content"]

        return "Unknown tool."
