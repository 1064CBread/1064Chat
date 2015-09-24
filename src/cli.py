if __name__ == '__main__':
    import sys

    sys.path.append('.')
    av = sys.argv
    if len(av) < 2:
        print('<command> <client|server>')
        sys.exit(1)
    if av[1] == 'client':
        import client

        print('Client NYI')
        sys.exit(2)
    elif av[1] == 'server':
        from server import app

        app.run()
