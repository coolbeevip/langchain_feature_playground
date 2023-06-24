import argparse

from waitress import serve

from service import api

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', type=str, default="0.0.0.0", help='Local Host')
    parser.add_argument('-P', '--port', type=int, default=5000, dest='port', help='Local Port')
    parser.add_argument('-d', '--debug', action='store_true', help='Debug Mode')
    args = parser.parse_args()

    if args.debug:
        api.app.run(debug=True)
    else:
        print(f'Started on {args.host}:{args.port}')
        serve(api.app, host=args.host, port=args.port)
