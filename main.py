from website import create_app #by default, all of the stuff in the __init__ file gets run, and we can import the contents of this file

app = create_app()

if __name__ == '__main__':
    app.run(debug = True)