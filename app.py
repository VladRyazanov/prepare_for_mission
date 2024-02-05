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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
