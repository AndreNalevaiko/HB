from gorillassite import wsgi

app = wsgi()

if __name__ == "__main__":

    app.run(debug=True)
