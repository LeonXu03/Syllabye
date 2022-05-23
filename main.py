from website import create_app #website is our python package, import create_app let's us access create_app() method

app = create_app()

if __name__ == '__main__': #only if we run main.py directly
    app.run(debug=True)

    