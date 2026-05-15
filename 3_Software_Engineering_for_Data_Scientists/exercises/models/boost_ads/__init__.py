from random import choice

posts = [{
      "user": "QuantumQuokka",
      "post": "Just tried to train my cat on a neural network. Now she’s only coming for treats with 95% accuracy. Still better than random forest! 🐱 #datascience #AI"
    },
    {
      "user": "StatisticalSquirrel",
      "post": "Why did the data scientist break up with their dataset? It had too many outliers. 😅 #datasciencejokes #outliers"
    },
    {
      "user": "LinearLemur",
      "post": "Tried to explain overfitting to my plants. Now they expect me to water them based on every leaf they grow. 🌱 #datascienceproblems #overfitting"
    },
    {
      "user": "BayesianBison",
      "post": "If my coffee consumption were a distribution, it’d definitely be skewed right ☕📊 #datascience #coffee #probability"
    },
    {
      "user": "ClusteringKoala",
      "post": "When you think your code will run in O(n) but it turns out to be O(n²). My poor CPU is crying. 🖥️😓 #datascience #algorithmwoes"
    },
    {
      "user": "RegressionRaccoon",
      "post": "My life is like k-means clustering: I’m trying to find the center of everything but still end up in the wrong group. 🤷‍♂️ #datascience #clustering"
    },
    {
      "user": "NeuralNarwhal",
      "post": "Running on 2 hours of sleep and 20 hidden layers. Both are overfitting at this point. 😴 #datasciencelife #AIproblems"
    },
    {
      "user": "DecisionTreeDingo",
      "post": "Every time someone says 'just visualize the data,' a scatter plot dies. 📉 #datascience #dataviz"
    },
    {
      "user": "LogisticLion",
      "post": "My relationship status: 'It's complicated'—Just like my logistic regression model. 💔 #datascience #logisticregression"
    },
    {
      "user": "RandomForestFox",
      "post": "Tried to make a random forest for my garden. Ended up with overfitting trees. 🌳 #datascience #gardeningfail"
    },
    ]

for entry in posts:
  entry['model'] = 'ads'

class BoostAdsModel:

    posts = posts
    __file__ = __file__

    def predict(self, user_id):

        return [choice(self.posts) for x in range(3)]
