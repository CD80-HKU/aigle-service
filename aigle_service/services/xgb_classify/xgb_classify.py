#import lightgbm as lgb
import pandas as pd
from xgboost import XGBClassifier, XGBRegressor
from xgboost import plot_importance
from aigle_service.services.train.data_instance import DataInstance
from sklearn.metrics import roc_curve
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler


def _xgb_classify(trainx, trainy, testx):
    t = XGBClassifier(learning_rate=0.01,
                      n_estimators=200,
                      max_depth=4,
                      min_child_weight=0.85,
                      gamma=0,
                      subsample=0.7,
                      eval_metric='auc')
    t.fit(trainx, trainy)
    y_pre = t.predict(testx)
    probas = t.predict_proba(testx)[:, 1]
    return y_pre, probas


def xgb_classify():
    data_instance = DataInstance()

    y_labeltest = data_instance.get_y_labeltest()

    data_train = data_instance.get_data_train()

    y_train = data_instance.get_y_train()

    data_test = data_instance.get_data_test()

    y_pre = []
    probas = []
    y_pre, probas = _xgb_classify(data_train, y_train, data_test)
#
    # 画ROC曲线的数据，df的第一列fpr是横轴，第二列tpr是纵轴
    fpr, tpr, _ = roc_curve(y_labeltest, probas)
    Roc_curve = {}
    Roc_curve = {'fpr': fpr, 'tpr': tpr}
    df_roc = pd.DataFrame(Roc_curve)

    t = XGBClassifier(learning_rate=0.01,
                      n_estimators=200,
                      max_depth=4,
                      min_child_weight=0.85,
                      gamma=0,
                      subsample=0.7,
                      eval_metric='auc').fit(data_train, y_train)

    model = SelectFromModel(t, prefit=True, threshold=0.003)
    feature_idx = model.get_support()
    feature_name = data_train.columns[feature_idx]
    feature_name = feature_name.tolist()

    # 画柱状图的，fplot是画图用的数据
    col = list(data_train.columns)
    lis = list(t.feature_importances_)
    f_importance = {}
    f_importance = {'col': col, 'lis': lis}
    f_importance = pd.DataFrame(f_importance)
    f_importance = f_importance.sort_values(by='lis', ascending=False)
    f_plot = f_importance.iloc[0:15, :]

    names = []

    for i in feature_name:
        names.append(i)
    new_model = data_train.loc[:, names]
    transfer = StandardScaler()
    new_model = pd.DataFrame(transfer.fit_transform(new_model))
    new_model.columns = names

    names = []
    for i in feature_name:
        names.append(i)
    test_new_model = data_test.loc[:, names]
    transfer = StandardScaler()
    test_new_model = pd.DataFrame(transfer.fit_transform(test_new_model))
    test_new_model.columns = names
