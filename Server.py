import asyncio
import random

class Server:
    pass

def main():
    server = Server()
    try:
        asyncio.run(server.run())
    except KeyboardInterrupt:
        print("Server interrotto da tastiera")


if __name__ == "__main__":
    main()
