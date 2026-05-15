from random import choice

posts = [

    {
      "user": "PythonPython",
      "post": "Me: I love clean code. Also me: Uses 10 nested loops in Python. 🐍 #datascience #pythonproblems"
    },
    {
      "user": "BayesBeetle",
      "post": "Bayes theorem is great and all, but how do I calculate the probability of me remembering to eat lunch today? 🥪 #datascience #Bayestheorem"
    },
    {
      "user": "AlgorithmAlpaca",
      "post": "Tried teaching my dog sorting algorithms. He’s more of a 'merge bones' kind of guy. 🐕 #datascience #algorithmjokes"
    },
    {
      "user": "LogLossLlama",
      "post": "Log loss? More like lost in the logs. Whoops. 📉🐾 #datascience #logloss"
    },
    {
      "user": "TuringTiger",
      "post": "Running a Turing test on my fridge to see if it’s secretly an AI... Still just holding snacks though. 🤖🍕 #datascience #AIjokes"
    },
    {
      "user": "OverfittingOcelot",
      "post": "Why did the machine learning model break up with the dataset? It was too clingy—overfitting much? 💔 #datascience #MLproblems"
    },
    {
      "user": "HyperparameterHawk",
      "post": "Is hyperparameter tuning just a fancy way of saying 'I’m guessing until it works'? 🎛️ #datascience #hyperparametertuning"
    },
    {
      "user": "ClusteringCrab",
      "post": "Every time I try to cluster data, I end up clustered with my coffee mug. ☕📊 #datascience #clusteringproblems"
    }
  ]

for entry in posts:
  entry['model'] = 'stable'


class StableModel:

    posts = posts
    __file__ = __file__

    def predict(self, user_id):

        return [choice(self.posts) for x in range(3)]
