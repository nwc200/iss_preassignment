from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    def choose_random_text():
        text_list = [
            "Logic will get you from A to B. Imagination will take you everywhere.",
            "There are 10 kinds of people. Those who know binary and those who don't.",
            "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
            "It's not that I'm so smart, it's just that I stay with problems longer.",
            "It is pitch dark. You are likely to be eaten by a grue."
        ]
        rand_num = random.randint(0, len(text_list)-1)
        return text_list[rand_num]

    text = choose_random_text()
    items = {
        "img_link": "https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "repo_link": "https://github.com/nwc200/iss_preassignment",
        "rand_text": text,
    }
    print(items)
    return render_template("index.html", **items)

if __name__ == "__main__":
    app.run()
