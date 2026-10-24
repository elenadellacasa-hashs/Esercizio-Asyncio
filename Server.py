import asyncio
import random

class Server:
    def __init__(self, host="0.0.0.0",port=2208):  # host = 0.0.0.0 vuol dire che il server accetta tutte le richiesta da qualsiasi indirizzo IP
        self.host = host
        self.port = port
        self.LED = "OFF"
        self.temp = 0
        self.umidita = 0

    async def client_connection(self, reader, writer):
        addr = writer.get_extra_info('peername')
        print(f"Connesso client {addr[0]} , {addr[1]}")
        try:
            while True:
                data = await reader.readline()
                if not data:
                    break

                comando = data.decode().strip().upper()

                if comando == "TEMP":
                    self.temp = round(random.uniform(15.0, 27.0), 1)
                    writer.write(f"OK temperatura = {self.temp}\n".encode())

                elif comando == "UMIDITA":
                    self.umidita = round(random.uniform(40.0, 65.0), 1)
                    writer.write(f"OK umidità = {self.umidita}%\n".encode())

                elif comando == "LED ON":
                    if self.LED == "ON":
                        writer.write(f"OK il LED era già {self.LED}\n".encode())
                    else:
                        self.LED = "ON"
                        writer.write(f"OK LED {self.LED}\n".encode())

                elif comando == "LED OFF":
                    if self.LED == "OFF":
                        writer.write(f"OK il LED era già {self.LED}\n".encode())
                    else:
                        self.LED = "OFF"
                        writer.write(f"OK LED {self.LED}\n".encode())

                elif comando == "STATO":
                    writer.write(f"OK temp = {self.temp} - umidità = {self.umidita}% - LED = {self.LED}\n".encode())

                elif comando == "QUIT":
                    writer.write(f"OK connessione chiusa\n".encode())
                    await writer.drain()
                    #per chiudere la connessione
                    writer.close()
                    await writer.wait_closed()
                    return

                else:
                    writer.write(f"ERR comando non riconosciuto\n".encode())
                await writer.drain()
        except Exception as e:
            print (f"Errore {e}")
        finally:
            writer.close()
            print(f"Client {addr[0]}, {addr[1]} disconnesso")


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
