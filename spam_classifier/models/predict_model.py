import pickle
from pathlib import Path

def load_the_model(filename):
    # load the model from disk
    artefacts_path = Path(__file__).parent / Path("artefacts")
    pickle_path = artefacts_path / Path(filename)
    loaded_model = pickle.load(open(pickle_path, 'rb'))
    return loaded_model


class SpamClassifier():
    def __init__(self):
        self.count_vector = load_the_model("count_vector.pkl")
        self.naive_bayes = load_the_model("naive_bayes.pkl")

    def predict(self, docs):
        return self.naive_bayes.predict(self.count_vector.transform(docs))
