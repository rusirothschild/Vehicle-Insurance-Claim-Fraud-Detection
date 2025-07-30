import numpy as np

class CV:
    def __init__(self, k: int, model, shuffle: bool=True, random_seed = None):
        self.k = k  
        self.model = model  
        self.shuffle = shuffle  
        self.random_seed = random_seed  

    def fit(self, X, y):
        np.random.seed(self.random_seed)

        self.X = np.array(X)
        self.y = np.array(y)

        fold_ids = []
        num_per_folds = len(X) // self.k
        remainder = len(X) % self.k
        num = 0
        rnum = 0
        for i in range(self.k):
          for j in range(num_per_folds):
            fold_ids.append(num)
          num = num + 1
        for r in range(remainder):
          fold_ids.append(rnum)
          rnum = rnum +1
        fold_ids = sorted(fold_ids)

        if self.shuffle:
            np.random.shuffle(fold_ids)

        fold_dict = {i: [] for i in range(self.k)}
        for idx, fold in enumerate(fold_ids):
          fold_dict[fold].append(idx)  

        test_data = []
        self.scores = []

        idx = 0
        for k in range(self.k):
            test_data = fold_dict[idx]
            train_data = [] # reset train_data for each fold
            for key in fold_dict:
                if key != idx:
                    train_data.extend(fold_dict[key])

            X_train = self.X[train_data]
            y_train = self.y[train_data]
            X_test = self.X[test_data]
            y_test = self.y[test_data]

            self.model.fit(X_train, y_train)
            self.scores.append(self.model.score(X_test, y_test))

            idx = idx + 1

        self.model.fit(self.X, self.y)

        return self 

    def predict(self, X): # Predicts using the fully trained model
        """
        This method takes a single parameter
            X: features, a two-dimensional array-like object with shape [m, d]

        and predicts y using a the fitted model
        """
        X = np.array(X)
        return  self.model.predict(X)

    def score(self, X, y): # Outputs the R^2 of the prediction.
        """
        Outputs the model's score method on X and y
        """
        X, y = np.array(X), np.array(y)
        return self.model.score(X, y)