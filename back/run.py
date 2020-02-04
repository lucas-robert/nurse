from back import create_app


if __name__ == "__main__":
    app = create_app()
    host = app.config.get("FLASK_HOST", "127.0.0.1")
    port = app.config.get("FLASK_PORT", 5000)
    servername = app.config["SERVER_NAME"]
    debug = app.config.get("DEBUG", True)
    print(f"Trying to launch Flask server on {host}:{port} with server_name {servername} (debug={debug})")

    mongo_host = app.config.get("MONGODB_HOST", None)
    mongo_port = app.config.get("MONGODB_PORT")
    mongo_db = app.config.get("MONGODB_DB")
    print(f"Using MongoDB URI: mongodb://{mongo_host}:{mongo_port}/{mongo_db}")

    print(f"Using Algo service URI: {app.config.get('ALGO_URI', None)}")
    app.run(host=host, port=port, debug=debug)
