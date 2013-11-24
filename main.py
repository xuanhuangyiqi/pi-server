import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class RadioHandler(tornado.web.RequestHandler):
    def get(self):
        radio_list = open('radio.txt').read().split('\n')
        radio_dic = {}
        print len(radio_list)
        for x in range(len(radio_list)/2):
            radio_dic[radio_list[x*2]] = radio_list[x*2+1]
        self.render("radio.html", radio=radio_dic)

class ShellHandler(tornado.web.RequestHandler):
    def get(self, befehl):
        if befehl == 'stop':
            self.write('stop')
            os.system("mpc stop")
        elif befehl == 'play':
            os.system("mpc add %s"%self.get_argument('url'))
            os.system("mpc play")
        else:
            self.write('else')

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/radio", RadioHandler),
    (r"/shell/(.*)", ShellHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "./static"}),
    ])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
