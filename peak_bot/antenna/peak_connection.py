import requests
import json

'''
Use to connect to a single Peak server.
'''
class PeakConnection():
    def open_session(self):
        session = requests.Session()
        session.get(self.login_url)
        self.data['csrfmiddlewaretoken']=session.cookies['csrftoken']
        return session

    def request_command(self, command_code):
        # Switch to HTTPS on BETA
        request_url = ('http://{0}/{1}/{2}/{3}/'.format(self.server_ip, 'library/commands', command_code,'download'))
        session=self.open_session()
        response = session.post(url=request_url, data=self.data, headers={'referer':self.login_url, 'Connection':'close'})
        return response.json()

    def update_profession(self, profession_code):
        # Switch to HTTPS on BETA
        request_url = ('http://{0}/{1}/{2}/{3}/'.format(self.server_ip, 'library/professions', profession_code, 'update'))
        session=self.open_session()
        response = session.post(url=request_url, data=self.data, headers={'referer':self.login_url, 'Connection':'close'})
        return response.json()

    def __init__(self, output_control, bot_data, connection_data):
        self.output_control = output_control
        self.data = dict(
            bot_name=bot_data['name'],
            bot_code=bot_data['code'],
            professions = bot_data['professions'],
            current_version=bot_data['version'],
            conn_code=connection_data['code'],
        )
        self.server_ip = connection_data['ip']
        self.login_url = ('http://{0}/{1}/'.format(self.server_ip, 'accounts/login'))
