class CFG():
    def __init__(self):
        self.token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyOTUzMjIxNyIsImlzcyI6IiIsImlhdCI6MTczMDAxMzMxNSwibmJmIjoxNzMwMDEzMzE1LCJleHAiOjE4ODc2OTMzMTV9.MX8eZZEJu0R6zLb8BKKQrO2z8EEoy6MRquwd-wSdpjc"
        self.img_server = "https://dg2ordyr4k5v3.cloudfront.net/"
        self.host = "https://d2dchjwa8oh2hv.cloudfront.net"
        self.title = "幼女"


if __name__ == '__main__':
    cfg = CFG()
    print(cfg.token)