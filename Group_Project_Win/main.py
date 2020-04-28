import storage
from GUI.connectWindow import ConnectWindow


def main():

    window = ConnectWindow()
    window.show()
    storage.app.exec_()


if __name__ == '__main__':
    main()