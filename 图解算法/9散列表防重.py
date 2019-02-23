voter = {}


def try_vote(name):
    if voter.get(name):
        return 'you have voted'
    else:
        voter[name] = True
        return 'thanks for voting'


print(try_vote('peter'))
print(try_vote('peter'))
