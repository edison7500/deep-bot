import re
import requests
from errbot import (BotPlugin,
                    arg_botcmd, botcmd, re_botcmd,
                    webhook)
from errbot.templating import tenv
from bottle import abort


class News(BotPlugin):

    @re_botcmd(pattern=r'^news(@deepto_bot)?', prefixed=False, flags=re.IGNORECASE)
    def news(self, msg, args):
        url = "https://api.chainnews.com/api/news/last_24.json"
        params = {
            'status': 'published'
        }
        res = requests.get(url, params=params)
        data = res.json()
        # response = tenv().get_template('news.j2').render(data=data)
        # if msg.is_group:
        #     return response
        # self.send(msg.frm, response,
        #           in_reply_to=msg, groupchat_nick_reply=True)
        # else:
        #     self.send(msg.frm, response)
        for row in data['results']:
            self.send_card(
                title=row['title'],
                body=row['content'],
                link=row['origin_link'],
                in_reply_to=msg,
            )

    @webhook('/news', methods=['POST'], raw=True)
    def push_news(self, request):
        # self.log.debug(repr(request))
        if not self.validate_incoming(request):
            abort(400)
        data = request.json
        response = tenv().get_template('news.j2').render(data=data)
        return self.send(self.build_identifier('@jiaxin'), response)

    @staticmethod
    def validate_incoming(request):
        """Validate the incoming request:
          Check if the payload decodes to something we expect
        """
        try:
            body = request.json
        except ValueError:
            return False
        if not isinstance(body, dict):
            return False
        return True
