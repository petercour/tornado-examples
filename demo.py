# -*- coding: utf-8 -*-

import tornado.ioloop 
import tornado.web

class HomeHandler(tornado.web.RequestHandler): 
    def get(self):
        self.write("hello, world")

class AboutHandler(tornado.web.RequestHandler): 
    def get(self):
        self.write("Mr President")

        
app = tornado.web.Application([
	(r"/", HomeHandler), 
	(r"/about", AboutHandler)
])
app.listen(8000)
tornado.ioloop.IOLoop.instance().start()
