#Kian AI

class KianAI:
    def __init__(self):
        self.name = "Kian AI"
        self.memory = []

    def greet(self):
        return f"سلام! من {self.name} هستم. چطور می توانم کمک کنم؟"

    def answer(self, question):
        question = question.lower()
        self.memory.append(question)
        if "اسم" in question:
            return f"اسم من {self.name} است."
        elif "سلام" in question:
            return "سلام! چطورید؟"
        elif "خداحافظ" in question:
            return "خداحافظ! موفق باشید."
        elif "حافظه" in question or "یادته" in question:
            return f"شما تا الان این ها را پرسیدید: {', '.join(self.memory[:-1])}" if self.memory[:-1] else "هنوز چیزی در حافظه ندارم."
        elif "چند سالته" in question:
            return "من یک هوش مصنوعی هستم و سن ندارم!"
        elif "چه کار می کنی" in question or "چه کاری بلدی" in question:
            return "من می توانم به سوالات ساده شما پاسخ دهم و مکالمه کنم."
        else:
            return "متاسفم، هنوز جواب این سوال را بلد نیستم."

# نمونه استفاده
if __name__ == "__main__":
    ai = KianAI()
    print(ai.greet())
    while True:
        user_input = input("شما: ")
        if user_input.lower() in ["خروج", "exit", "خداحافظ"]:
            print(ai.answer("خداحافظ"))
            break
        print("Kian AI:", ai.answer(user_input))