from flask_failsafe import failsafe


@failsafe
def create_app():
    from app import manager
    return manager


if __name__ == '__main__':
	app = create_app()
	port = int(app.config['PORT'])

	app.run(host='0.0.0.0', port=port)
