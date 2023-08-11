from Lesson_24.websites_ping import WebSitePing


if __name__ == "__main__":
    command = WebSitePing()
    result = command.get_ping(["www.google.com", "www.ithillel.ua"], 3)
    command.print_result(result)
