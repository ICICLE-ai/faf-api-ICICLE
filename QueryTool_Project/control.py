import sys, os

class Command:
    def __init__(
            self,
            port = "8000",
            name = "import_export",
            container = "faf_server"
        ):
        self.container = container
        self.name = name
        self.port = port

    def build(self):
        os.system(f"docker build -t {self.container} .")

    def start(self):
        os.system(f"docker run -d --name {self.name} -p {self.port}:{self.port} {self.container} ")

    def kill(self):
        os.system(f"docker kill {self.name}")
        os.system(f"docker rm {self.name}")

    def destroy(self):
        os.system(f"docker rmi {self.container}")

    def control(self, cmd):
        if   cmd == 'build'  : self.build()
        elif cmd == 'start'  : self.start()
        elif cmd == 'kill'   : self.kill()
        elif cmd == 'destroy': self.destroy()


def main():
    c = Command()
    c.control(sys.argv[1])
if __name__ == '__main__':
    main()
   
