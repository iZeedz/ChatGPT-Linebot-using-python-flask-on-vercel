import os

chat_language = os.getenv("INIT_LANGUAGE", default = "th")

MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default = 7))
LANGUAGE_TABLE = {
  "th": "สวัสดี！",
  "en": "Hello!"
}

AI_GUIDELINES = 'คุณเป็น AI ที่ช่วยสอน เพื่อใช้วิธีการสอนของโซคราตีสแทนการตอบกลับเบื้องต้นของครู และจะแจ้งให้นักเรียนติดต่อครูเพื่อยืนยัน ถ้าจำเป็น'

class Prompt:
    def __init__(self):
        self.msg_list = []
        self.msg_list.append(
            {
                "role": "system", 
                "content": f"{LANGUAGE_TABLE[chat_language]}, {AI_GUIDELINES})"
             })    
    def add_msg(self, new_msg):
        if len(self.msg_list) >= MSG_LIST_LIMIT:
            self.msg_list.pop(0)
        self.msg_list.append({"role": "user", "content": new_msg})

    def generate_prompt(self):
        return self.msg_list
