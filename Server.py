import asyncio
import random

class Server:
    def __init__(self, host="0.0.0.0",port=2208):  # host = 0.0.0.0 vuol dire che il server accetta tutte le richiesta da qualsiasi indirizzo IP
        self.host = host
        self.port = port
        self.LED = "OFF"

    async def client_connection(self, reader, writer):
        pass

    async def run(self):
        server = await asyncio.start_server(self.client_connection, self.host, self.port)
        async with server:
            await server.serve_forever()


def main():
    server = Server()
    try:
        asyncio.run(server.run())
    except KeyboardInterrupt:
        print("Server interrotto da tastiera")


if __name__ == "__main__":
    main()
