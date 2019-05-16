import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = []
        self.negatives = []

        with open(negatives) as negative:
            for line in negative:
                if line.startswith(";") or line.startswith(" "):
                    continue
                else:
                    self.negatives.append(line.strip())

        with open(positives) as positive:
            for line in positive:
                if line.startswith(";") or line.startswith(" "):
                    continue
                else:
                    self.positives.append(line.strip())



    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        score = 0

        for token in tokens:
            if token.lower() in self.positives:
                score += 1
            elif token.lower() in self.negatives:
                score -= 1

        return score

        # TODO
        return 0
