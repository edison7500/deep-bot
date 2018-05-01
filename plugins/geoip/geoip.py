import geoip2.database
from errbot import BotPlugin, arg_botcmd
from errbot.templating import tenv


class Geoip(BotPlugin):

    def activate(self):
        path = self.bot_config.GEOIP_PATH
        self.reader = geoip2.database.Reader(path)
        # self.reader = geoip2.database.Reader("/Users/xiejiaxin/PycharmProjects/jiaxin.im/2b/GeoLite2-City_20180403/GeoLite2-City.mmdb")
        super().activate()

    def deactivate(self):
        self.reader.close()
        super().deactivate()

    @arg_botcmd('--ip', type=str)  # flags a command
    def find(self, mess, ip):  # a command callable with !tryme
        res = self.reader.city(ip)
        country = res.country.names['zh-CN']
        response = tenv().get_template('geoip_res.md').render(res=res, country=country)
        self.send(mess.frm, response)
