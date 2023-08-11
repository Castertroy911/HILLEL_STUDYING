import subprocess
import sys


class WebSitePing:

    def __init__(self):
        self.__win_command = "ping -n {} {}"
        self.__linux_command = "ping -с {} {}"

    def get_ping(self, urls: list, requests_number: int) -> list:
        platform = sys.platform
        output = []
        for url in urls:
            if platform == "win32":
                result = subprocess.run(self.__win_command.format(requests_number, url), stdout=subprocess.PIPE)
                result = result.stdout.decode(encoding="cp866")
                output.append(result)
            elif platform == "linux":
                result = subprocess.run(self.__linux_command.format(requests_number, url))
                result = result.stdout.decode(encoding="UTF 8")
                output.append(result)
        return output

    @staticmethod
    def print_result(result):
        for _ in result:
            print(_)


