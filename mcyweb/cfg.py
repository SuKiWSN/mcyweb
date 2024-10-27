class CFG():
    def __init__(self):
        self.token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyOTUzMjIxNyIsImlzcyI6IiIsImlhdCI6MTczMDAyMjg3MiwibmJmIjoxNzMwMDIyODcyLCJleHAiOjE4ODc3MDI4NzJ9.BifuR8g-k2qFFxZCXshhn2u-FY-WT0TsGNHq496MFV0"
        self.img_server = "https://dg2ordyr4k5v3.cloudfront.net/"
        self.host = "https://d2dchjwa8oh2hv.cloudfront.net"
        self.title = "幼女"


if __name__ == '__main__':
    cfg = CFG()
    print(cfg.token)