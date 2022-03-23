""" Basic todo list using webpy 0.3 """
import web
import os
import sys
import package2.tmscrap as tmscrap
import package2.tmscrap2 as tmscrap2

### Url mappings

urls = (
        "/", "Index",
        "/del/(\d+)", "Delete",
        "/tongyong", "TongYong"
        )

def get_current_dir():
    dirname1, filename1 = os.path.split(os.path.realpath(__file__))
    print("todo running from", dirname1)
    return dirname1

current_dir = get_current_dir()

### Templates
render = web.template.render(os.path.join(current_dir, "templates"), base="base")


class Index:

    form = web.form.Form(
        web.form.Textbox("title", description="技术关键字:"),
        web.form.Button("查询"),
    )

    def GET(self):
        form = self.form()
        todos = tmscrap.search_timu('')
        # print(todos)
        return render.index(todos, form)

    def POST(self):
        """ Add new entry """
        form = self.form()
        form.validates()
        key = form.d.title.strip() if form.d.title is not None else ''
        print("key: ", key)
        todos = tmscrap.search_timu(key)
        # print(todos)
        return render.index(todos, form)


class TongYong:

    form = web.form.Form(
        web.form.Textbox("title", description="通用关键字:"),
        web.form.Button("查询"),
    )

    def GET(self):
        form = self.form()
        todos = tmscrap2.search_timu('')
        # print(todos)
        return render.tongyong(todos, form)

    def POST(self):
        """ Add new entry """
        form = self.form()
        form.validates()
        key = form.d.title.strip() if form.d.title is not None else ''
        print("key: ", key)
        todos = tmscrap2.search_timu(key)
        # print(todos)
        return render.tongyong(todos, form)

class Delete:
    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        raise web.seeother("/")


def main():
    app = web.application(urls, globals())
    sys.argv.append('0.0.0.0:8081')
    app.run()


if __name__ == "__main__":
    main()
