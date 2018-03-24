import math


def get_key_from_value(my_dict, v):
    for key,value in my_dict.items():
        if value == v:
            return key
    return None

class Classifier:
    
    def __init__(self, outcomes):
        # Prepare outcome object list
        self.outcomes = { }
        for outcome in outcomes:
            self.outcomes[outcome] = Outcome()

    def add_training_example(self, outcome, tokens):
        self.outcomes[outcome].add_training_example(tokens)
    
    def outcome(self, outcome):
	# Compute outcome probabilities
        return float(self.outcomes[outcome].count) / sum(
            [outcome_obj.count for outcome_name, outcome_obj in self.outcomes.iteritems()])

    def tokens(self, tokens):
	# Token probabilities
        return sum([outcome_obj.tokens_given_outcome(tokens) 
                    for outcome_name, outcome_obj in self.outcomes.iteritems()])

    def outcome_given_token(self, token, outcome):
	# Compute P(O | T) for outcome O and token T.
        token_probability = (
            sum([self.outcomes[other_outcome].token_given_outcome(token) *
                 self.outcome(other_outcome)
                 for other_outcome in self.outcomes.keys()]))
        if token_probability <= 0.0000001:
            return 0.0
        # Bayes formula
        return (
            self.outcomes[outcome].token_given_outcome(token) *
            self.outcome(outcome) / token_probability)

    def outcome_given_tokens(self, tokens, outcome):
        """Give P(O | T1 & T2 & ... & Tn) for outcome O and tokens Ti."""
        # For each token, calculate the probability of the outcome
        probabilities = [self.outcome_given_token(token, outcome)
                         for token in tokens]
        # Combine the probabilities using sigmoid to avoid floating point underflow,
        # and ignore prboabilities of 1 or 0 which cause the answer to be undefined
        exponent = sum([math.log(1 - p) - math.log(p)
                        for p in probabilities if p != 0 and p != 1])
        return 1.0 / (1 + math.exp(exponent))

    def classify_tokens(self, tokens):
        """Find the probability of each outcome given a set of tokens."""
        outcome_probabilities = dict(
            [(outcome, self.outcome_given_tokens(tokens, outcome))
             for outcome in self.outcomes.keys()])
        return outcome_probabilities

    def most_likely_outcome(self, tokens):
        """Find the most likely outcome given a set of tokens."""
        return max(self.outcomes.keys(), 
            key=lambda outcome: self.outcome_given_tokens(tokens, outcome))

    def get_top_features(self):
        feat_list = {}
    	for outcome in self.outcomes:
    		feat_list[outcome] = (self.outcomes[outcome].get_max_features())
        return feat_list

    def print_feat(self):
    	for outcome in self.outcomes.keys():
    		print 'Features for outcome'
    		print outcome
    		self.outcomes[outcome].print_dict()
    		print'\n\n'


class Outcome:

    def __init__(self):
        self.token_counts = { }
        self.count = 0

    def add_training_example(self, tokens):
        # Increment the outcome count
        self.count += 1
        # Increment the count of every token
        for token in tokens:
            if self.token_counts.has_key(token):
                self.token_counts[token] += 1
            else:
                self.token_counts[token] = 1
    
    def token_given_outcome(self, token):
        # Give P(T | O) for token T and this outcome O.
        if self.token_counts.has_key(token):
            return float(self.token_counts[token]) / self.count
        else:
            return 0.0

    def get_max_features(self):
        c=0
        feat_list = {}
        for item in reversed(sorted(self.token_counts.values())):
            val = item
            key = get_key_from_value(self.token_counts,item)
            feat_list[key] = val
            c+=1
            if(c>=20):
                break
        return feat_list

    def print_dict(self):
    	c=0
    	for feat in self.token_counts.keys():
    		print self.token_counts[feat]
    		c+=1
    		if(c>=5):
    			break
