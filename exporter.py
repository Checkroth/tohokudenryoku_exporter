import sys


class DenryokuExporter:
    def __init__(
            self,
            login_id: str,
            contract_name: str,
            postal_code: str,
            phone_number: str,
    ):
        self.login_id1, self.login_id2, self.login_id3 = login_id.split('-')
        self.contract_name = contract_name
        self.postal_code1, self.postal_code2 = postal_code.split('-')
        self.phone_number1, self.phone_number2, self.phone_number3 = phone_number.split('-')

    def login(self):
        url = (
            'https://www8.zf1.tohoku-epco.co.jp/'
            '?satk=at202109231900249974f5b8-6ead-4633-ab87-d417599b65ab'
        )
        form_body = {
            'nId1': '010',
            'contents_0$txtLoginId2': self.login_id1,
            'contents_0$txtLoginId3': self.login_id2,
            'contents_0$txtLoginId4': self.login_id3,
            'contents_0$txtContractNmKana': self.contract_name,
            'contents_0$txtZipTop': self.postal_code1,
            'contents_0$txtZipLower': self.postal_code2,
            'contents_0$txtTelAreaCode': self.phone_number1,
            'contents_0$txtTelLocalCode': self.phone_number2,
            'contents_0$txtTelSubscriberNumber': self.phone_number3,
            'contents_0$chkHdLoginContinuation': 'on',
            'contents_0$addressAutoSchAncId': '',
            'contents_0$iptLogin': '',
            # Below: needed? who knows
            # 'satk': 'at202109231900249974f5b8-6ead-4633-ab87-d417599b65ab',
            # 'Tran_token': '',
        }
        resp = requests.post(url, json=form_body)

    def serve(self):
        self.login()


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 4:
        print(
            'exporter required four arguments in this order:\n '
            'LOGIN_ID, CONTRACT_NAME, POSTAL_CODE, PHONE_NUMBER'
        )
        return
    exporter = DenryokuExporter(*args)
    exporter.serve()
