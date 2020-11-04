from sklearn import svm
import pandas as pd
from sklearn.model_selection import GridSearchCV,ParameterGrid
from sklearn.base import clone
from sklearn.cluster import AffinityPropagation
from sklearn import metrics
import numpy as np
import joblib
import datetime
import matplotlib.pyplot as plt
import xlwt
from sklearn.model_selection import learning_curve

class svm:
    def para_input(self):
        para = pd.read_excel("para.xlsx", header=None, dtype='object')
        dic = para.set_index(0).T.to_dict('list')
        for i in dic:
            dic[i] = [x for x in dic[i] if x == x]
        return dic

    def write_wrong_label(self,classifier, data_list, label_list, filename):  # Output error classification samples
        predict_label_list = classifier.predict(data_list)
        j = 0
        wrong_file = xlwt.Workbook(encoding='utf-8')
        wrong_sheet = wrong_file.add_sheet(u'sheet1', cell_overwrite_ok=True)

        for i in range(len(data_list)):
            if predict_label_list[i] != label_list[i]:
                j = j + 1
                wrong_sheet.write(j, 0, i + 1)

        wrong_sheet.write(0, 0, 'Total category error')
        wrong_sheet.write(0, 1, j)
        wrong_file.save(filename)

    def SVMGridsearch(self,dmodel, data, labels, param_dict):
        """
          dmodel: default model
          data：training data
          labels: real classification
          param_dict: hyperparameter combination dictionary
        """
        output_models = []

        # create parameter grid
        # create hyperparametric grid
        param_grid = ParameterGrid(param_dict)

        # change the parameter attributes in dbscan according to the param_grid
        #  According to the hyperparameters of the grid, modify the corresponding parameters of DBSCAN object, train the model, and get the output data
        for param in param_grid:
            for key, value in param.items():
                setattr(dmodel, key, value)

            dmodel.fit(data, labels)
            model = clone(dmodel)
            output_models.append(model)
        # If you have other data to output, just add it 
        return (output_models)

    def get_marks(self,estimator, data, labels, name=None):
        """
            To get the score, there are five kinds of actual classification information that are required to know the data set, and there are three kinds that are not required,
       refer to the readme.txt
       
    :param estimator: model
    :param name: initial method
    :param data: feature data set
        """
        estimator.fit(data.astype(np.float64), labels)
        res = estimator.predict(data)
        print(30 * '*', name, 30 * '*')
        print("Model and parameters       : ", estimator)
        print("Homogeneity Score         : ", metrics.homogeneity_score(labels, res))
        print("Completeness Score        : ", metrics.completeness_score(labels, res))
        print("V-Measure Score           : ", metrics.v_measure_score(labels, res))
        print("Adjusted Rand Score       : ", metrics.adjusted_rand_score(labels, res))
        print("Adjusted Mutual Info Score: ", metrics.adjusted_mutual_info_score(labels, res))
        print("Calinski Harabasz Score   :   ", metrics.calinski_harabasz_score(data, res))
        print("Silhouette Score          : ", metrics.silhouette_score(data, res))

    def plot_learning_curve(self,model, data, labels):
        train_sizes, train_scores, test_scores = learning_curve(model, data, labels,
                                                                scoring='adjusted_rand_score', cv=5)
        train_scores_mean = np.mean(train_scores, axis=1)  #Average the training score set by row 
        train_scores_std = np.std(train_scores, axis=1)  #Calculate the standard deviation of training matrix 
        test_scores_mean = np.mean(test_scores, axis=1)
        test_scores_std = np.std(test_scores, axis=1)
        plt.grid()  # set the background to gridlines

        plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std,
                         alpha=0.1,
                         color='r')
        # plt.fill_between()function fills the space of the upper and lower variances of the average model accuracy with colors.
        plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.1,
                         color='g')
        plt.plot(train_sizes, train_scores_mean, 'o-', color='r', label='Training score')
        # Then use plt.plot The () function to draw the average of the model accuracy
        plt.plot(train_sizes, test_scores_mean, 'o-', color='g', label='Cross_validation score')
        plt.legend(loc='best')  #show legend 
        plt.show()
