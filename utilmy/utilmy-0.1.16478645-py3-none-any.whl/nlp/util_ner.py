# -*- coding: utf-8 -*-
MNAME = "utilmy.nlp.util_ner"
HELP = """ utils for




"""
import os, sys, glob, time,gc, datetime, numpy as np, pandas as pd
from typing import List, Optional, Tuple, Union
from numpy import ndarray
from box import Box






#############################################################################################
from utilmy import log, log2

def help():
    """function help"""
    from utilmy import help_create
    print( HELP + help_create(MNAME) )



#############################################################################################
def test_all() -> None:
    """function test_all

    """
    log(MNAME)
    test1()
    test2()


def test1() -> None:
    """function test1
    Args:
    Returns:

    """
    pass




def test2() -> None:
    """function test2
    Args:
    Returns:

    """
    pass

#############################################################################################






###############################################################################
#                            NER                                              #
###############################################################################

def ner_displacy(txt, ner=None, lst_tag_filter=None, title=None, serve=False):
    '''
    Display the spacy NER model.
    :parameter
        :param txt: string - text input for the model.
        :param model: string - "en_core_web_lg", "en_core_web_sm", "xx_ent_wiki_sm"
        :param lst_tag_filter: list or None - example ["ORG", "GPE", "LOC"], None for all tags
        :param title: str or None
    '''
    ner = spacy.load("en_core_web_lg") if ner is None else ner
    doc = ner(txt)
    doc.user_data["title"] = title
    if serve == True:
        spacy.displacy.serve(doc, style="ent", options={"ents":lst_tag_filter})
    else:
        spacy.displacy.render(doc, style="ent", options={"ents":lst_tag_filter})



def utils_ner_text(txt, ner=None, lst_tag_filter=None, grams_join="_"):
    '''
    Find entities in text, replace strings with tags and extract tags:
        Donald Trump --> Donald_Trump
        [Donald Trump, PERSON]
    '''
    ## apply model
    ner = spacy.load("en_core_web_lg") if ner is None else ner
    entities = ner(txt).ents

    ## tag text
    tagged_txt = txt
    for tag in entities:
        if (lst_tag_filter is None) or (tag.label_ in lst_tag_filter):
            try:
                tagged_txt = re.sub(tag.text, grams_join.join(tag.text.split()), tagged_txt) #it breaks with wild characters like *+
            except Exception as e:
                continue

    ## extract tags list
    if lst_tag_filter is None:
        lst_tags = [(tag.text, tag.label_) for tag in entities]  #list(set([(word.text, word.label_) for word in ner(x).ents]))
    else:
        lst_tags = [(word.text, word.label_) for word in entities if word.label_ in lst_tag_filter]

    return tagged_txt, lst_tags



def utils_lst_count(lst, top=None):
    '''
    Counts the elements in a list.
    :parameter
        :param lst: list
        :param top: num - number of top elements to return
    :return
        lst_top - list with top elements
    '''
    dic_counter = collections.Counter()
    for x in lst:
        dic_counter[x] += 1
    dic_counter = collections.OrderedDict(sorted(dic_counter.items(), key=lambda x: x[1], reverse=True))
    lst_top = [ {key:value} for key,value in dic_counter.items() ]
    if top is not None:
        lst_top = lst_top[:top]
    return lst_top



def utils_ner_features(lst_dics_tuples, tag):
    '''
    Creates columns
        :param lst_dics_tuples: [{('Texas','GPE'):1}, {('Trump','PERSON'):3}]
        :param tag: string - 'PERSON'
    :return
        int
    '''
    if len(lst_dics_tuples) > 0:
        tag_type = []
        for dic_tuples in lst_dics_tuples:
            for tuple in dic_tuples:
                type, n = tuple[1], dic_tuples[tuple]
                tag_type = tag_type + [type]*n
                dic_counter = collections.Counter()
                for x in tag_type:
                    dic_counter[x] += 1
        return dic_counter[tag]   #pd.DataFrame([dic_counter])
    else:
        return 0



def add_ner_spacy(data, column, ner=None, lst_tag_filter=None, grams_join="_", create_features=True):
    '''
    Apply spacy NER model and add tag features.
    :parameter
        :param dtf: dataframe - dtf with a text column
        :param column: string - name of column containing text
        :param ner: spacy object - "en_core_web_lg", "en_core_web_sm", "xx_ent_wiki_sm"
        :param lst_tag_filter: list - ["ORG","PERSON","NORP","GPE","EVENT", ...]. If None takes all
        :param grams_join: string - "_", " ", or more (ex. "new york" --> "new_york")
        :param create_features: bool - create columns with category features
    :return
        dtf
    '''
    ner = spacy.load("en_core_web_lg") if ner is None else ner
    dtf = data.copy()

    ## tag text and exctract tags
    print("--- tagging ---")
    dtf[[column+"_tagged", "tags"]] = dtf[[column]].apply(lambda x: utils_ner_text(x[0], ner, lst_tag_filter, grams_join),
                                                          axis=1, result_type='expand')

    ## put all tags in a column
    print("--- counting tags ---")
    dtf["tags"] = dtf["tags"].apply(lambda x: utils_lst_count(x, top=None))

    ## extract features
    if create_features == True:
        print("--- creating features ---")
        ### features set
        tags_set = []
        for lst in dtf["tags"].tolist():
            for dic in lst:
                for k in dic.keys():
                    tags_set.append(k[1])
        tags_set = list(set(tags_set))
        ### create columns
        for feature in tags_set:
            dtf["tags_"+feature] = dtf["tags"].apply(lambda x: utils_ner_features(x, feature))
    return dtf



def tags_freq(tags, top=30, figsize=(10,5)):
    '''
    Compute frequency of spacy tags.
    '''
    tags_list = tags.sum()
    map_lst = list(map(lambda x: list(x.keys())[0], tags_list))
    dtf_tags = pd.DataFrame(map_lst, columns=['tag','type'])
    dtf_tags["count"] = 1
    dtf_tags = dtf_tags.groupby(['type','tag']).count().reset_index().sort_values("count", ascending=False)
    fig, ax = plt.subplots(figsize=figsize)
    fig.suptitle("Top frequent tags", fontsize=12)
    sns.barplot(x="count", y="tag", hue="type", data=dtf_tags.iloc[:top,:], dodge=False, ax=ax)
    ax.set(ylabel=None)
    ax.grid(axis="x")
    plt.show()
    return dtf_tags



def retrain_ner_spacy(train_data, output_dir, model="blank", n_iter=100):
    '''
    Retrain spacy NER model with new tags.
    :parameter
        :param train_data: list [
                ("Who is Shaka Khan?", {"entities": [(7, 17, "PERSON")]}),
                ("I like London and Berlin.", {"entities": [(7, 13, "LOC"), (18, 24, "LOC")]}),
            ]
        :param output_dir: string - path of directory to save model
        :param model: string - "blanck" or "en_core_web_lg", ...
        :param n_iter: num - number of iteration
    '''
    try:
        ## prepare data
#        train_data = []
#        for name in lst:
#            frase = "ciao la mia azienda si chiama "+name+" e fa business"
#            tupla = (frase, {"entities":[(30, 30+len(name), tag_type)]})
#            train_data.append(tupla)

        ## load model
        if model == "blank":
            ner_model = spacy.blank("en")
        else:
            ner_model = spacy.load(model)

        ## create a new pipe
        if "ner" not in ner_model.pipe_names:
            new_pipe = ner_model.create_pipe("ner")
            ner_model.add_pipe(new_pipe, last=True)
        else:
            new_pipe = ner_model.get_pipe("ner")

        ## add label
        for _, annotations in train_data:
            for ent in annotations.get("entities"):
                new_pipe.add_label(ent[2])

        ## train
        other_pipes = [pipe for pipe in ner_model.pipe_names if pipe != "ner"] ###ignora altre pipe
        with ner_model.disable_pipes(*other_pipes):
            print("--- Training spacy ---")
            if model == "blank":
                ner_model.begin_training()
            for n in range(n_iter):
                random.shuffle(train_data)
                losses = {}
                batches = spacy.util.minibatch(train_data, size=spacy.util.compounding(4., 32., 1.001)) ###batch up data using spaCy's minibatch
                for batch in batches:
                    texts, annotations = zip(*batch)
                    ner_model.update(docs=texts, golds=annotations, drop=0.5, losses=losses)  ###update

        ## test the trained model
        print("--- Test new model ---")
        for text, _ in train_data:
            doc = ner_model(text)
            print([(ent.text, ent.label_) for ent in doc.ents])

        ## save model to output directory
        ner_model.to_disk(output_dir)
        print("Saved model to", output_dir)

    except Exception as e:
        print("--- got error ---")
        print(e)



###############################################################################
#             MODEL DESIGN & TESTING - MULTILABEL CLASSIFICATION              #
###############################################################################

def dtf_partitioning(dtf, y, test_size=0.3, shuffle=False):
    '''
    Split the dataframe into train / test
    '''
    dtf_train, dtf_test = model_selection.train_test_split(dtf, test_size=test_size, shuffle=shuffle)
    print("X_train shape:", dtf_train.drop(y, axis=1).shape, "| X_test shape:", dtf_test.drop(y, axis=1).shape)
    print("y:")
    for i in dtf_train["y"].value_counts(normalize=True).index:
        print(" ", i, " -->  train:", round(dtf_train["y"].value_counts(normalize=True).loc[i], 2),
                          "| test:", round(dtf_test["y"].value_counts(normalize=True).loc[i], 2))
    print(dtf_train.shape[1], "features:", dtf_train.drop(y, axis=1).columns.to_list())
    return dtf_train, dtf_test



def add_encode_variable(dtf, column):
    '''
    Transform an array of strings into an array of int.
    '''
    dtf[column+"_id"] = dtf[column].factorize(sort=True)[0]
    dic_class_mapping = dict( dtf[[column+"_id",column]].drop_duplicates().sort_values(column+"_id").values )
    return dtf, dic_class_mapping



def evaluate_multi_classif(y_test, predicted, predicted_prob, figsize=(15,5)):
    '''
    Evaluates a model performance.
    :parameter
        :param y_test: array
        :param predicted: array
        :param predicted_prob: array
        :param figsize: tuple - plot setting
    '''
    classes = np.unique(y_test)
    y_test_array = pd.get_dummies(y_test, drop_first=False).values

    ## Accuracy, Precision, Recall
    accuracy = metrics.accuracy_score(y_test, predicted)
    auc = metrics.roc_auc_score(y_test, predicted_prob, multi_class="ovr")
    print("Accuracy:",  round(accuracy,2))
    print("Auc:", round(auc,2))
    print("Detail:")
    print(metrics.classification_report(y_test, predicted))

    ## Plot confusion matrix
    cm = metrics.confusion_matrix(y_test, predicted)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', ax=ax, cmap=plt.cm.Blues, cbar=False)
    ax.set(xlabel="Pred", ylabel="True", xticklabels=classes, yticklabels=classes, title="Confusion matrix")
    plt.yticks(rotation=0)

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=figsize)
    ## Plot roc
    for i in range(len(classes)):
        fpr, tpr, thresholds = metrics.roc_curve(y_test_array[:,i], predicted_prob[:,i])
        ax[0].plot(fpr, tpr, lw=3, label='{0} (area={1:0.2f})'.format(classes[i], metrics.auc(fpr, tpr)))
    ax[0].plot([0,1], [0,1], color='navy', lw=3, linestyle='--')
    ax[0].set(xlim=[-0.05,1.0], ylim=[0.0,1.05], xlabel='False Positive Rate',
              ylabel="True Positive Rate (Recall)", title="Receiver operating characteristic")
    ax[0].legend(loc="lower right")
    ax[0].grid(True)

    ## Plot precision-recall curve
    for i in range(len(classes)):
        precision, recall, thresholds = metrics.precision_recall_curve(y_test_array[:,i], predicted_prob[:,i])
        ax[1].plot(recall, precision, lw=3, label='{0} (area={1:0.2f})'.format(classes[i], metrics.auc(recall, precision)))
    ax[1].set(xlim=[0.0,1.05], ylim=[0.0,1.05], xlabel='Recall', ylabel="Precision", title="Precision-Recall curve")
    ax[1].legend(loc="best")
    ax[1].grid(True)
    plt.show()






































###################################################################################################
if __name__ == "__main__":
    import fire
    fire.Fire()


