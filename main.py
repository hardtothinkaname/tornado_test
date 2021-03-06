import tornado.ioloop
import tornado.web
from PIL import Image
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello, world")


class InputTest(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", 'admin')

        self.write("hello, " + name)


class PostImg(tornado.web.RequestHandler):
    def get(self):
        form = '''
<html>
  <head><title>Upload File</title></head>
  <body>
    <form action='postimg' enctype="multipart/form-data" method='post'>
    <input type='file' name='file'/><br/>
    <input type='submit' value='submit'/>
    </form>
  </body>
</html>
'''
        self.write(form)
        print("return")

        pass

    def post(self):
        # 这部分就是上传的文件,想要查看更多可以print self.request看看
        # 该文件返回一个元素为字典的列表
        upload_path = os.path.join(os.path.dirname(__file__), 'files')  # 文件的暂存路径
        if not os.path.exists(upload_path):
            os.mkdir(upload_path)


        file_metas = self.request.files['file']  # 提取表单中‘name’为‘file’的文件元数据
        for meta in file_metas:
            filename = meta['filename']
            filepath = os.path.join(upload_path, filename)
            with open(filepath, 'wb') as up:  # 有些文件需要已二进制的形式存储，实际中可以更改
                up.write(meta['body'])
            self.write('finished!')


            # im = Image.open(img['body'])



def make_app():
    return tornado.web.Application(
        [(r"/", MainHandler),
         (r"/inputtest", InputTest),
         (r"/postimg", PostImg),
         ]
    )





if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

