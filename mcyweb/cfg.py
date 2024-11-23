class CFG():
    def __init__(self):
        self.token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyOTUzMjIxNyIsImlzcyI6IiIsImlhdCI6MTczMjM0NzcxNSwibmJmIjoxNzMyMzQ3NzE1LCJleHAiOjE4OTAwMjc3MTV9.gsoTVmzOZfNZuVaijy8_vYfSt6bqW50BtCyrfYXl1dQ"
        self.img_server = "https://dg2ordyr4k5v3.cloudfront.net/"
        self.host = "https://d2dchjwa8oh2hv.cloudfront.net"
        self.title = "幼女"


if __name__ == '__main__':
    cfg = CFG()
    print(cfg.token)