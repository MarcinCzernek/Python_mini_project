import pickle

file = "address.dat"

def start():
    print


def save_data(contacts, file):
    savefile = open(file, 'b')
    pickle.dump(contacts, savefile)
    savefile.close()
    print("Saved to file...")

def load_data(file):
    loadfile = open(file, 'rb')
    book = pickle.load(loadfile)
    loadfile.close()
    print("File loaded...")
    return book
