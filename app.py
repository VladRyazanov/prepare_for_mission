from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
    return render_template("base.html", page_title=title)


@app.route("/training/<prof>")
def training(prof):
    if "строитель" in prof or "инженер" in prof:
        return render_template("training.html", prof="инженер")
    return render_template("training.html")


@app.route("/list_prof/<type_of_list>")
def list_prof(type_of_list):
    return render_template("list_prof.html", type_of_list=type_of_list)


@app.route("/answer")
@app.route("/auto_answer")
def answer():
    page_title = "Анкета"
    data = {
        "Фамилия": "Watny",
        "Имя": "Mark",
        "Образование": "Выше среднего",
        "Профессия": "Штурман марсохода",
        "Пол": "male",
        "Мотивация": "Всегда мечтал застрять на Марсе!",
        "Готовы остаться на Марсе": "True"}
    keys_and_data = [{"title": i, "data": data[i]} for i in data.keys()]
    return render_template("answer.html", keys_and_data=keys_and_data, page_title=page_title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
