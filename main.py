if __name__=="__main__":
    from spam_classifier import SpamClassifier

    sc = SpamClassifier()
    print(sc.predict(['Free free free hurry come on',
                      'free credit card offer 2000 discount get airbus for free',
                      'hope you are fine']))