class CFG():
    def __init__(self):
        self.token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyOTUzMjIxNyIsImlzcyI6IiIsImlhdCI6MTcyOTIxODg2MywibmJmIjoxNzI5MjE4ODYzLCJleHAiOjE4ODY4OTg4NjN9.3e4uMHbvZ5dk9sOJV4Dz72CuxNtDMvtzSBjcgYAJm3w"
        self.img_server = "https://dg2ordyr4k5v3.cloudfront.net/"
        self.host = "https://d2dchjwa8oh2hv.cloudfront.net"


if __name__ == '__main__':
    cfg = CFG()
    print(cfg.token)