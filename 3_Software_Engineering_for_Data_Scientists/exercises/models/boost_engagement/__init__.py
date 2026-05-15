from random import choice

posts = [

    {
      "user": "PandasPenguin",
      "post": "Is it just me, or does wrangling data in pandas feel like playing 3D chess with Excel? ♟️🐼 #datascience #pandas"
    },
    {
      "user": "SQLSloth",
      "post": "SELECT * FROM fridge WHERE item = 'snacks'; — Guess it’s time to run my favorite query. 🍫 #SQL #datascience #snacktime"
    },
    {
      "user": "DeepLearningDolphin",
      "post": "Tried to explain deep learning to my dog. Now she’s looking at me like I’m speaking in tensors. 🐕🤖 #datascience #deeplearning"
    },
    {
      "user": "MatrixMongoose",
      "post": "Why did the matrix apply for a job? Because it had too many dimensions to handle on its own! 🧮 #datascience #matrixjokes"
    },
    {
      "user": "FeatureFlamingo",
      "post": "Tried to add 'sense of humor' as a feature to my model. Now it just tells dad jokes. 🤖😂 #datascience #featureengineering"
    },
    {
      "user": "GradientGiraffe",
      "post": "Why did the neural network go to therapy? It had issues with convergence. 🧠💥 #datascience #neuralnetworkjokes"
    },
    {
      "user": "OverfitOtter",
      "post": "My predictive model said I would be at the gym today... I guess it’s just overfitting my past data. 🏋️‍♂️📉 #datascience #overfitting"
    },
    {
      "user": "BigDataBison",
      "post": "People: 'Big data will change the world.' Me: 'Cool, but can it change my sleep schedule?' 😴 #datascience #bigdata"
    },
    {
      "user": "OutlierOwl",
      "post": "Everyone’s talking about normal distributions while I’m over here just trying to be an outlier. 📊🦉 #datascience #outlierlife"
    },
    {
      "user": "ArtificialAntelope",
      "post": "Training a model on 1 million data points but can’t remember where I left my keys... 🤔🔑 #datasciencelife #forgetful"
    },
    {
      "user": "CorrelationCrow",
      "post": "Correlation may not imply causation, but not having coffee directly correlates with my lack of productivity. ☕ #datascience #correlation"
    },
]

for entry in posts:
  entry['model'] = 'engagement'

class BoostEngagementModel:

    posts = posts
    __file__ = __file__

    def predict(self, user_id):

        return [choice(self.posts) for x in range(3)]