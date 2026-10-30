from http.server import BaseHTTPRequestHandler, HTTPServer
import json

planets = [
    {
        "name": "Земля",
        "type": "Каменистая планета",
        "distance": "149,6 млн км"
    },
    {
        "name": "Марс",
        "type": "Каменистая планета",
        "distance": "227,9 млн км"
    },
    {
        "name": "Юпитер",
        "type": "Газовый гигант",
        "distance": "778,5 млн км"
    }
]


class PlanetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/planets":

            response = json.dumps(planets, ensure_ascii=False, indent=2)
            response_bytes = response.encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(response_bytes)))
            self.end_headers()
            self.wfile.write(response_bytes)
        else:

            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("404 Not Found".encode("utf-8"))


def run():
    host = "127.0.0.1"
    port = 8000
    server = HTTPServer((host, port), PlanetHandler)
    print(f"Сервер запущен: http://{host}:{port}/planets")
    print("Для остановки нажмите Ctrl+C")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен")
        server.server_close()


if __name__ == "__main__":
    run()