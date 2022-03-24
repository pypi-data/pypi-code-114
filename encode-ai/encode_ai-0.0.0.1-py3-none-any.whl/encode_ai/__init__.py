# __init__.py
def get_ann():
    code = '''
    # Importing Packages
    import numpy as np
    import pandas as pd 
    import keras
    from keras.models import Sequential
    from keras.layers import Dense,Dropout
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import MinMaxScaler
    import keras
    import tensorflow as tf
    import matplotlib.pyplot as plt

    # Importing Data
    df_diabetes = pd.read_csv("../input/diabetes/diabetes.csv")

    # Data Overview
    df_diabetes.head()

    # Dataset Details
    df_diabetes.describe()

    # Dataset Shape
    df_diabetes.shape

    # Independent Dependent Variables Split
    X = df_diabetes.drop("Outcome",axis = 1)
    Y = df_diabetes["Outcome"]

    # Train Test SPlit
    X_train, X_test,y_train,y_test = train_test_split(X,Y,test_size = 0.25,random_state = 27)

    # Scaling
    scaler = MinMaxScaler()
    scaled_train = scaler.fit_transform(X_train)
    scaled_test = scaler.transform(X_test)

    ## NN MODEl
    model = Sequential()
    model.add(Dense(512, activation='relu', input_shape=(X.shape[1],)))
    model.add(Dropout(0.5))
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.25))
    model.add(Dense(1, activation='sigmoid'))

    # Compiling the model
    model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = 0.001),
                loss=keras.losses.BinaryCrossentropy(from_logits=True),
                metrics=["accuracy"])

    # Fitting train,test data in the model
    history = model.fit(X_train,y_train,epochs=100,validation_data=(X_test,y_test),batch_size = 64)

    # Model Structure Overview
    model.summary()

    # Plotting accuracy of train,test
    def plot_metric(history, metric):
        train_metrics = history.history[metric]
        val_metrics = history.history['val_'+metric]
        epochs = range(1, len(train_metrics) + 1)
        plt.plot(epochs, train_metrics)
        plt.plot(epochs, val_metrics)
        plt.title('Training and validation '+ metric)
        plt.xlabel("Epochs")
        plt.ylabel(metric)
        plt.legend(["train_"+metric, 'val_'+metric])
        plt.show()

    # Checking acccuracy graph
    plot_metric(history,"accuracy")'''
    print(code)


def get_ann_encoded():
    code = '''
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import category_encoders as ce
    from keras.models import Sequential
    from keras.layers import Dense
    from sklearn.model_selection import train_test_split

    data=pd.read_csv("/content/drive/MyDrive/mushroom_dataset/mushrooms.csv")
    data.head()
    data.shape

    df=pd.get_dummies(data,data.columns,drop_first=True)
    X=df.drop(['class_p'],axis=1)
    y=df['class_p']

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
    X_train,X_val,y_train,y_val=train_test_split(X_train,y_train,test_size=0.3,random_state=0)
    X_train.shape

    model=Sequential()
    model.add(Dense(12,input_dim=95,activation='relu'))
    model.add(Dense(8,activation='relu'))
    model.add(Dense(1,activation='sigmoid'))
    model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    model.fit(X_train,y_train,epochs=50,batch_size=10,validation_data=(X_val,y_val))
    model.summary()

    y_pred=model.predict(X_test)
    y_pred=(y_pred>0.5)
    y_pred

    from sklearn.metrics import accuracy_score,confusion_matrix
    score=accuracy_score(y_test,y_pred)
    cm=confusion_matrix(y_test,y_pred)
    print(cm)
    '''
    print(code)

def get_cnn_bw():
    code = '''
    from keras.datasets import mnist
    from keras.models import Sequential
    from keras.layers import Dense,Dropout,Conv2D,MaxPool2D,Flatten
    from keras.utils import np_utils
    import numpy as np

    (X_train,y_train),(X_test,y_test)=mnist.load_data()

    X_train.shape

    from sklearn.model_selection import train_test_split
    X_train,X_val,y_train,y_val=train_test_split(X_train,y_train,test_size=0.3,random_state=0)

    X_train=X_train.reshape(X_train.shape[0],28,28,1)
    X_test=X_test.reshape(X_test.shape[0],28,28,1)
    X_val=X_val.reshape(X_val.shape[0],28,28,1)

    X_train=X_train.astype('float32')
    X_val=X_val.astype('float32')
    X_test=X_test.astype('float32')

    X_train=X_train/255
    X_val=X_val/255
    X_test=X_test/255

    n_classes=10
    print("Shape before one-hot encoding: ",y_train.shape)
    Y_train=np_utils.to_categorical(y_train,n_classes)
    Y_val=np_utils.to_categorical(y_val,n_classes)
    Y_test=np_utils.to_categorical(y_test,n_classes)
    print("Shape after one-hot encoding: ",Y_train.shape)
    print("Shape after one-hot encoding: ",Y_val.shape)

    model=Sequential()
    model.add(Conv2D(32,kernel_size=(3,3),strides=(1,1),padding='valid',activation='relu',input_shape=X_train.shape[1:]))
    model.add(MaxPool2D(pool_size=(2,2)))
    model.add(Flatten())
    model.add(Dense(100,activation='relu'))
    model.add(Dense(10,activation='softmax'))

    model.compile(loss='categorical_crossentropy',metrics=['accuracy'],optimizer='adam')

    history=model.fit(X_train,Y_train,epochs=2,batch_size=400,validation_data=(X_val,Y_val))

    import matplotlib.pyplot as plt
    acc=history.history['accuracy']
    val_acc=history.history['val_accuracy']
    epochs=range(1,3)
    plt.plot(epochs,acc,label='accuracy')
    plt.plot(epochs,val_acc,label='Validation Accuracy')
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.show()

    loss=history.history['loss']
    val_loss=history.history['val_loss']
    epochs=range(1,3)
    plt.plot(epochs,loss,label='loss')
    plt.plot(epochs,val_loss,label='Validation loss')
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.show()

    y_pred=model.predict(X_test)
    y_pred=(y_pred>0.5)
    y_pred

    Y_pred=np.argmax((y_pred>0.5),axis=1)
    print(Y_pred)
    print(y_test)

    Y_test

    from sklearn.metrics import accuracy_score,confusion_matrix

    score=accuracy_score(Y_test,y_pred)
    score

    import seaborn as sns
    cm=confusion_matrix(y_test,Y_pred)
    sns.heatmap(cm,annot=True)
    '''
    print(code)

def get_cnn_rgb():
    code = '''
    from keras.datasets import cifar10
    from keras.layers import Dense,Flatten,MaxPool2D,Conv2D
    from keras.models import Sequential

    (X_train,y_train),(X_test,y_test)=cifar10.load_data()

    X_train.shape

    from sklearn.model_selection import train_test_split
    X_train,X_val,y_train,y_val=train_test_split(X_train,y_train,test_size=0.3,random_state=0)

    X_train=X_train.astype('float32')
    X_val=X_val.astype('float32')
    X_test=X_test.astype('float32')

    X_train=X_train/255
    X_test=X_test/255
    X_val=X_val/255

    from keras.utils import np_utils

    y_train=np_utils.to_categorical(y_train)
    y_val=np_utils.to_categorical(y_val)
    y_test=np_utils.to_categorical(y_test)

    X_train.shape

    model=Sequential()

    model.add(Conv2D(32,kernel_size=(4,4),activation='relu',input_shape=X_train.shape[1:],padding='valid'))
    model.add(MaxPool2D(pool_size=(3,3)))
    model.add(Flatten())
    model.add(Dense(64,activation='relu'))
    model.add(Dense(32,activation='relu'))
    model.add(Dense(10,activation='softmax'))

    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

    history=model.fit(X_train,y_train,epochs=2,batch_size=200,validation_data=(X_val,y_val))

    y_pred=model.predict(X_test)
    y_pred=(y_pred>0.5)
    y_pred

    y_test

    from sklearn.metrics import accuracy_score,confusion_matrix

    score=accuracy_score(y_test,y_pred)
    score

    import matplotlib.pyplot as plt

    acc=history.history['accuracy']
    val_acc=history.history['val_accuracy']
    epochs=range(1,3)
    plt.plot(epochs,acc,label="accuracy")
    plt.plot(epochs,val_acc,label='val_accuracy')
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.show()

    train_loss=history.history['loss']
    val_loss=history.history['val_loss']
    epochs=range(1,3)
    plt.plot(epochs,train_loss,label="loss")
    plt.plot(epochs,val_loss,label='val_loss')
    plt.xlabel("Epochs")
    plt.ylabel("loss")
    plt.legend()
    plt.show()
    '''
    print(code)

def get_alexnet():
    code = '''
    import tensorflow
    from tensorflow.keras.layers import Dense, Activation, Dropout, Flatten,Conv2D, MaxPooling2D,BatchNormalization
    from tensorflow.keras.models import Model
    from tensorflow.keras.applications.vgg16 import VGG16
    from tensorflow.keras.applications.vgg19 import VGG19
    from tensorflow.keras.preprocessing import image
    from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img
    from tensorflow.keras.datasets import mnist
    from tensorflow.keras.models import Sequential
    from sklearn.model_selection import train_test_split
    from keras.datasets import cifar10
    from keras.utils import np_utils
    from keras.preprocessing.image import ImageDataGenerator
    import numpy as np
    import keras


    (X_train,Y_train),(X_test,Y_test) = cifar10.load_data()


    X_train,X_val,Y_train,Y_val = train_test_split(X_train,Y_train,test_size = 0.3)


    Y_train = np_utils.to_categorical(Y_train)
    Y_test = np_utils.to_categorical(Y_test)
    Y_val = np_utils.to_categorical(Y_val)


    train_generator = ImageDataGenerator(rotation_range=2, horizontal_flip=True,zoom_range=.1 )
    
    val_generator = ImageDataGenerator(rotation_range=2, horizontal_flip=True,zoom_range=.1)
    
    test_generator = ImageDataGenerator(rotation_range=2, horizontal_flip= True,zoom_range=.1)


    train_generator.fit(X_train)
    val_generator.fit(X_val)
    test_generator.fit(X_test)


    model = keras.models.Sequential([
        keras.layers.Conv2D(filters=96, kernel_size=(11,11), strides=(1,1), activation='relu', input_shape=(32,32,3)),
        keras.layers.BatchNormalization(),
        keras.layers.MaxPool2D(pool_size=(3,3), strides=(2,2)),
        keras.layers.Conv2D(filters=256, kernel_size=(5,5), strides=(1,1), activation='relu', padding="same"),
        keras.layers.BatchNormalization(),
        keras.layers.MaxPool2D(pool_size=(3,3), strides=(2,2)),
        keras.layers.Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), activation='relu', padding="same"),
        keras.layers.BatchNormalization(),
        keras.layers.Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), activation='relu', padding="same"),
        keras.layers.BatchNormalization(),
        keras.layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), activation='relu', padding="same"),
        keras.layers.BatchNormalization(),
        keras.layers.MaxPool2D(pool_size=(3,3), strides=(2,2)),
        keras.layers.Flatten(),
        keras.layers.Dense(4096, activation='relu'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(2048, activation='relu'),
        keras.layers.Dropout(0.1),
        keras.layers.Dense(1024, activation='relu'),
        keras.layers.Dropout(0.1),
        keras.layers.Dense(512, activation='relu'),
        keras.layers.Dropout(0.1),
        keras.layers.Dense(256, activation='relu'),
        keras.layers.Dropout(0.1),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dropout(0.1),
        keras.layers.Dense(10, activation='softmax')
    ])


    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

    model.fit_generator(train_generator.flow(X_train,Y_train,batch_size = 1024),epochs = 20,
                        steps_per_epoch = len(X_train)//1024,validation_data = val_generator.flow(X_val,Y_val,batch_size = 1024),verbose = 1)

    '''
    print(code)

def get_resnet():
    code = '''
    
    import numpy as np
    import pandas as pd
    from sklearn.utils.multiclass import unique_labels
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import seaborn as sns
    get_ipython().run_line_magic('matplotlib', 'inline')
    import itertools
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix
    from keras import Sequential
    from tensorflow.keras.applications.resnet50 import ResNet50
    from keras.preprocessing.image import ImageDataGenerator
    from tensorflow.keras.optimizers import SGD,Adam
    from keras.callbacks import ReduceLROnPlateau
    from keras.layers import Flatten,Dense,BatchNormalization,Activation,Dropout
    from keras.utils.np_utils import to_categorical
    from keras.datasets import cifar10

    (x_train,y_train),(x_test,y_test)=cifar10.load_data()

    x_train,x_val,y_train,y_val=train_test_split(x_train,y_train,test_size=.3)

    #Print the dimensions of the datasets to make sure everything's kosher

    print((x_train.shape,y_train.shape))
    print((x_val.shape,y_val.shape))
    print((x_test.shape,y_test.shape))

    #One hot encode the labels.Since we have 10 classes we should expect the shape[1] of y_train,y_val and y_test to change from 1 to 10

    y_train=to_categorical(y_train)
    y_val=to_categorical(y_val)
    y_test=to_categorical(y_test)

    # Lets print the dimensions one more time to see if things changed the way we expected

    print((x_train.shape,y_train.shape))
    print((x_val.shape,y_val.shape))
    print((x_test.shape,y_test.shape))

    #Data Augmentation Function: Let's define an instance of the ImageDataGenerator class and set the parameters.We have to instantiate for the Train,Validation and Test datasets
    train_generator = ImageDataGenerator(
                                        rotation_range=2, 
                                        horizontal_flip=True,
                                        zoom_range=.1 )

    val_generator = ImageDataGenerator(
                                        rotation_range=2, 
                                        horizontal_flip=True,
                                        zoom_range=.1)

    test_generator = ImageDataGenerator(
                                        rotation_range=2, 
                                        horizontal_flip= True,
                                        zoom_range=.1) 

    #Fit the augmentation method to the data

    train_generator.fit(x_train)
    val_generator.fit(x_val)
    test_generator.fit(x_test)

    lrr= ReduceLROnPlateau(
                        monitor='val_acc', #Metric to be measured
                        factor=.01, #Factor by which learning rate will be reduced
                        patience=3,  #No. of epochs after which if there is no improvement in the val_acc, the learning rate is reduced
                        min_lr=1e-5) #The minimum learning rate 

    base_model_2 = ResNet50(include_top=False,weights='imagenet',input_shape=(32,32,3),classes=y_train.shape[1])


    #Since we have already defined Resnet50 as base_model_2, let us build the sequential model.

    model_2=Sequential()
    #Add the Dense layers along with activation and batch normalization
    model_2.add(base_model_2)
    model_2.add(Flatten())


    #Add the Dense layers along with activation and batch normalization
    model_2.add(Dense(4000,activation=('relu'),input_dim=512))
    model_2.add(Dense(2000,activation=('relu'))) 
    model_2.add(Dropout(.4))
    model_2.add(Dense(1000,activation=('relu'))) 
    model_2.add(Dropout(.3))#Adding a dropout layer that will randomly drop 30% of the weights
    model_2.add(Dense(500,activation=('relu')))
    model_2.add(Dropout(.2))
    model_2.add(Dense(10,activation=('softmax'))) #This is the classification layer

    model_2.summary()

    model_2.compile(optimizer="adam",loss='categorical_crossentropy',metrics=['accuracy'])

    model_2.fit_generator(train_generator.flow(x_train,y_train,batch_size=100),
                        epochs=10,steps_per_epoch=x_train.shape[0]//100,
                        validation_data=val_generator.flow(x_val,y_val,batch_size=100),validation_steps=250,callbacks=[lrr])

    y_pred_resnet=np.argmax(model_2.predict(x_test), axis=-1)
    y_true=np.argmax(y_test,axis=1)

    #Compute the confusion matrix
    confusion_mtx=confusion_matrix(y_true,y_pred_resnet)

    class_names=['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    def plot_confusion_matrix(y_true, y_pred, classes,
                            normalize=False,
                            title=None,
                            cmap=plt.cm.Blues):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        if not title:
            if normalize:
                title = 'Normalized confusion matrix'
            else:
                title = 'Confusion matrix, without normalization'

        # Compute confusion matrix
        cm = confusion_matrix(y_true, y_pred)
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')

    #     print(cm)

        fig, ax = plt.subplots(figsize=(14,14))
        im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
        ax.figure.colorbar(im, ax=ax)
        # We want to show all ticks...
        ax.set(xticks=np.arange(cm.shape[1]),
            yticks=np.arange(cm.shape[0]),
            # ... and label them with the respective list entries
            xticklabels=classes, yticklabels=classes,
            title=title,
            ylabel='True label',
            xlabel='Predicted label')

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                rotation_mode="anchor")
        # Loop over data dimensions and create text annotations.
        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i in range(cm.shape[0]):
            for j in range(cm.shape[1]):
                ax.text(j, i, format(cm[i, j], fmt),
                        ha="center", va="center",
                        color="white" if cm[i, j] > thresh else "black")
        fig.tight_layout()
        return ax


    np.set_printoptions(precision=2)


    # Plot non-normalized confusion matrix
    plot_confusion_matrix(y_true, y_pred_resnet, classes=class_names,title='Confusion matrix, without normalization')

    '''
    print(code)

def get_googlenet():
    code = '''
        
    import keras
    from keras.layers import Dense, Dropout, MaxPool2D, Conv2D, Flatten, Concatenate, Input, GlobalAveragePooling2D
    from keras.models import Model
    from tensorflow.keras.optimizers import Adam
    from tensorflow.keras.models import load_model
    from tensorflow.keras.applications.inception_v3 import InceptionV3
    import cv2
    import matplotlib.pyplot as plt
    from sklearn.metrics import confusion_matrix

    def inception_block(x,f):
    t1 = Conv2D(f[0],1,activation="relu")(x)
    
    t2 = Conv2D(f[1],1,activation="relu")(x)
    t2 = Conv2D(f[2],3,padding="same",activation="relu")(t2)
    
    t3 = Conv2D(f[3],1,activation="relu")(x)
    t3 = Conv2D(f[4],5,padding="same",activation="relu")(t3)

    t4 = MaxPool2D(3,1,padding="same")(x)
    t4 = Conv2D(f[5],1,activation="relu")(t4)

    output = Concatenate()([t1,t2,t3,t4])
    return output


    input = Input(shape = (224,224,3))
    x = Conv2D(64, 7, strides = 2, padding = "same", activation = "relu")(input)
    x = MaxPool2D(3, 2, padding="same")(x)
    x = Conv2D(64, 1, activation = "relu")(x)
    x = Conv2D(192, 3, padding="same", activation = "relu")(x)
    x = MaxPool2D(3, 2, padding="same")(x)
    x = inception_block(x, [64,96,128,16,32,32])


    from keras.preprocessing.image import ImageDataGenerator



    train_generator = ImageDataGenerator(rescale = 1/255, horizontal_flip = False, validation_split = 0.2)
    test_generator = ImageDataGenerator(rescale = 1/255, horizontal_flip = False)


    train_path = "../input/dogs-vs-cats/train"
    test_path = "../input/dogs-vs-cats/test"

    train_dataset = train_generator.flow_from_directory(
        train_path,
        batch_size = 128,
        target_size = (224,224),
        class_mode = "binary",
        color_mode = "rgb",
        subset = "training")

    validation_dataset = train_generator.flow_from_directory(
        train_path,
        batch_size = 128,
        target_size = (224,224),
        class_mode = "binary",
        color_mode = "rgb",
        subset = "validation")

    test_dataset = train_generator.flow_from_directory(
        test_path,
        batch_size = 128,
        target_size = (224,224),
        class_mode = "binary",
        color_mode = "rgb",)

    import matplotlib.pyplot as plt
    import numpy as np
    train_dataset[0][0].shape


    model = InceptionV3(input_shape = (224,224,3), weights = "imagenet", include_top = False)

    batch_size = 128
    num_classes = 1


    for layers in model.layers:
    layers.trainable = False

    x = model.output
    x = GlobalAveragePooling2D()(x)
    x = Flatten()(x)
    x = Dense(512,activation="relu")(x)
    prediction = Dense(num_classes,activation = "sigmoid")(x)
    model = Model(model.input, prediction)
    model.summary()
    model.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = "accuracy")

    history = model.fit_generator(train_dataset, validation_data = validation_dataset, epochs = 3, shuffle = True)


    model.evaluate_generator(test_dataset)

    model.save("inception_model.h5")

    history = history.history
    plt.plot(history["accuracy"])
    plt.plot(history["val_accuracy"])
    plt.title("Accuracy Plot")
    plt.xlabel("epoch")
    plt.ylabel("accuracy")
    plt.legend(["train","val"])
    plt.savefig("accuracy.png")

    plt.plot(history["loss"])
    plt.plot(history["val_loss"])
    plt.title("Loss Plot")
    plt.xlabel("epoch")
    plt.ylabel("loss")
    plt.legend(["train","val"])
    plt.savefig("loss.png")

    get_ipython().system('wget https://scx2.b-cdn.net/gfx/news/hires/2018/2-dog.jpg')

    img = cv2.imread('2-dog.jpg')
    image = cv2.resize(img, (224, 224))
    plt.imshow(img)

    model = load_model('inception_model.h5')

    round(model.predict(np.array([image]))[0][0])

    train_dataset.class_indices

    y_pred = model.predict_generator(test_dataset)

    pred = y_pred.argmax(axis = 1)


    confusion_matrix(test_dataset.classes,pred)
    '''
    print(code)


def get_vgg16():
    code = '''
    from keras.preprocessing.image import ImageDataGenerator
    import keras
    from keras.applications.vgg16 import VGG16
    from keras.layers import Flatten, Dense, Dropout
    import matplotlib.pyplot as plt


    train_datagen = ImageDataGenerator(
        rescale = 1./255,
    )

    test_datagen = ImageDataGenerator(
        rescale = 1./255,
    )

    training_set = train_datagen.flow_from_directory(
        '/content/drive/MyDrive/CSE360_DeepLearning_Code/DAY - 4/Data/Pneumonia Dataset/train',
        target_size = (224,244),
        # color_mode = "grayscale",
        batch_size = 32,
        class_mode = "binary"
        )

    testing_set = test_datagen.flow_from_directory(
        '/content/drive/MyDrive/CSE360_DeepLearning_Code/DAY - 4/Data/Pneumonia Dataset/test',
        target_size = (224,244),
        # color_mode = "grayscale",
        batch_size = 32,
        class_mode = "binary"
        )

    model = VGG16(
        input_shape = (244,244,3),
        include_top = False,
        weights = 'imagenet'
        )

    for layers in model.layers:
    layers.trainable = False


    x = Flatten()(model.output)
    x = Dense(4096, activation = "relu")(x)
    x = Dropout(0.2)(x)
    x = Dense(4096, activation = "relu")(x)
    x = Dropout(0.2)(x)
    x = Dense(4096, activation = "relu")(x)
    x = Dropout(0.2)(x)
    x = Dense(1, activation = "sigmoid")(x)

    model = keras.Model(model.input, x)
    model.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = "accuracy")
    model.summary()


    hist = model.fit_generator(training_set,validation_data = testing_set, epochs = 1)


    hist = hist.history


    plt.plot(hist["accuracy"])
    plt.plot(hist["val_accuracy"])
    plt.title("Accuracy plot")
    plt.legend(["train","test"])
    plt.xlabel("epoch")
    plt.ylabel("accuracy")

    plt.plot(hist["loss"])
    plt.plot(hist["val_loss"])
    plt.title("Accuracy loss")
    plt.legend(["train","test"])
    plt.xlabel("epoch")
    plt.ylabel("loss")

    '''
    print(code)


def get_lstm_imdb():
    code = '''
    from keras.datasets import imdb
    from keras import Sequential
    from keras.layers import Embedding, LSTM, Dense, Dropout
    vocabulary_size = 5000
    (X_train, y_train), (X_test, y_test) = imdb.load_data(num_words = vocabulary_size)
    print('Loaded dataset with {} training samples,{} test samples'.format(len(X_train), len(X_test)))
    print('---review---')
    print(X_train[6])
    print('---label---')
    print(y_train[6])
    word2id = imdb.get_word_index()
    id2word = {i: word for word, i in word2id.items()}
    print('---review with words---')
    print([id2word.get(i, ' ') for i in X_train[6]])
    print('---label---')
    print(y_train[6])
    print('Maximum review length: {}'.format(len(max((X_train + X_test), key=len))))
    print('Minimum review length: {}'.format(len(min((X_test + X_test), key=len))))
    from keras.preprocessing import sequence
    max_words = 500
    X_train = sequence.pad_sequences(X_train, maxlen=max_words)
    X_test = sequence.pad_sequences(X_test, maxlen=max_words)
    embedding_size=32
    model=Sequential()
    model.add(Embedding(vocabulary_size, embedding_size, input_length=max_words))
    model.add(LSTM(100))
    model.add(Dense(1, activation='sigmoid'))
    print(model.summary())
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    batch_size = 64
    num_epochs = 3
    X_valid, y_valid = X_train[:batch_size], y_train[:batch_size]
    X_train2, y_train2 = X_train[batch_size:], y_train[batch_size:]
    model.fit(X_train2, y_train2, validation_data=(X_valid, y_valid),
            batch_size=batch_size, epochs=num_epochs)
    scores = model.evaluate(X_test, y_test, verbose=0)
    print('Test accuracy:', scores[1])
    '''
    print(code)

def get_lstm_stock():
    code = '''
    # Importing Packages
    import numpy as np
    import pandas as pd
    from pandas_datareader.data import DataReader
    import yfinance as yf
    from datetime import datetime
    import math
    from sklearn.preprocessing import MinMaxScaler
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, LSTM, Dropout
    from sklearn.metrics import mean_squared_error
    import matplotlib.pyplot as plt
    import tensorflow as tf

    # Scrapping GOOG Data
    df = DataReader('GOOG',data_source='yahoo',start='2000-1-1',end='2022-03-03')

    # Filtering only Close feature
    data = df.filter(['Close'])

    # Converting dataframe to numpy array
    dataset = data.values

    # Defining train dataset length
    training_data_len = math.ceil(len(dataset) * .8)

    # Min Max Scaler 
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)

    # Splitting train data
    training_data = scaled_data[0:training_data_len, :]

    # X_train, Y_train Split
    x_train = []
    y_train = []
    for i in range(60, len(training_data)):
        x_train.append(training_data[i-60:i, 0])
        y_train.append(training_data[i, 0])
        if i <= 61:
            print(x_train)
            print(y_train)
            
    # Converting them to array
    x_train, y_train = np.array(x_train), np.array(y_train)

    # Reshaping X Train
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # Model Building
    model = Sequential()
    model.add(LSTM(128, return_sequences=True ,input_shape=(x_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(88, return_sequences=True))
    model.add(LSTM(48, return_sequences=False))
    model.add(Dense(128, activation='relu'))
    # model.add(Dropout(0.2))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(1, activation='linear'))

    # Model Summary
    model.summary()

    # Compiling the model
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(loss='mean_squared_error', optimizer=optimizer)

    # Fiiting the model
    model.fit(x_train, y_train, batch_size=32, epochs=50)

    # Splitting Test Data
    test_data = scaled_data[training_data_len:, :]
    X_test = []
    Y_test = []

    for i in range(60,len(test_data)):
        X_test.append(test_data[i-60:i, 0])
        Y_test.append(test_data[i, 0])

    X_test, Y_test = np.array(X_test), np.array(Y_test)

    # Reshaping Test Data
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    # Predictions using Test Data
    preds = model.predict(X_test)

    # Applying inverse trans
    preds = scaler.inverse_transform(preds)

    # Finding RMSE Value
    rmse = np.sqrt(mean_squared_error(Y_test, preds))

    # Train Val Seperation
    train = data[:training_data_len]
    valid = data[training_data_len+60:]

    # Appending predictions made by model
    valid['Predictions'] = preds

    # Plot for comparing Validation Data & Test Data
    plt.figure(figsize=(16,8))
    plt.title('Model')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.plot(train['Close'])
    plt.plot(valid[['Close', 'Predictions']])
    plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
    plt.show()
    '''
    print(code)

def get_lstm_gender():
    code = '''
    # Impoting Packages
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import string

    # Impoting Data
    data=pd.read_csv("../input/national-names/NationalNames.csv")

    data.shape
    data.head()
    data['Gender']=data['Gender'].astype('category').cat.codes
    data.head()
    df= data.groupby('Name').mean()['Gender'].reset_index()
    df.shape
    df['Gender']=df['Gender'].astype('int')
    letters=list(string.ascii_lowercase)
    letters
    vocab=dict(zip(letters,range(1,27)))
    vocab
    r_vocab=dict(zip(range(1,27),letters))
    r_vocab
    def word_to_number():
        for i  in range(0,df.shape[0]):
            seq=[ vocab[letters.lower()] for letters in df['Name'][i]]
            df['Name'][i]=seq
    # to convert our names to list of equivalent numbers
    word_to_number()
    X=df['Name'].values
    Y=df['Gender'].values
    name_length=[len(X[i]) for i in range (0, df.shape[0])]
    plt.hist(name_length,bins=20)
    plt.show()
    from keras.preprocessing.sequence import pad_sequences
    x=pad_sequences(df['Name'].values,
                    maxlen=10,
                    padding='pre')

    #build the model
    from keras.layers import Input,Embedding,Dense,LSTM
    from keras.models import Model
    vocab_size=len(vocab)+1
    input=Input(shape=(10,))
    emn=Embedding(input_dim=vocab_size,output_dim=5)(input)
    lstm1=LSTM(units=32,return_sequences=True)(emn)
    lstm2=LSTM(units=64)(lstm1)
    out=Dense(units=1,activation='sigmoid')(lstm2)
    my_model=Model(inputs=input,outputs=out)
    #build the model
    from keras.layers import Input,Embedding,Dense,LSTM
    from keras.models import Model
    vocab_size=len(vocab)+1
    input=Input(shape=(10,))
    emn=Embedding(input_dim=vocab_size,output_dim=5)(input)
    lstm1=LSTM(units=32,return_sequences=True)(emn)
    lstm2=LSTM(units=64)(lstm1)
    out=Dense(units=1,activation='sigmoid')(lstm2)
    my_model=Model(inputs=input,outputs=out)
    my_model.summary()
    my_model.compile(optimizer='adam',
                    loss='binary_crossentropy',
                    metrics=['acc'])

    his=my_model.fit(x,Y,epochs=10, batch_size=256,validation_split=0.2)

    fig, ax=plt.subplots(nrows=1,ncols=1,figsize=(10,5))
    ax.plot(his.history['acc'],label='Accuracy')
    ax.plot(his.history['val_acc'],label='Validation Accuracy')
    ax.legend()
    fig.show()

    fig, ax=plt.subplots(nrows=1,ncols=1,figsize=(10,5))
    ax.plot(his.history['loss'],label='Loss')
    ax.plot(his.history['val_loss'],label='Validation Loss')
    ax.legend()
    fig.show()

    def predict_name(name):
        test_name=name.lower()
        seq=[vocab[i] for i in test_name]
        x_test=pad_sequences([seq],10)
        y_pred=my_model.predict(x_test)
        if y_pred < 0.5:
            print("Name is female...")
        else:
            print("Name is male...")
    predict_name('Ugur')
    '''
    print(code)

def get_vanilla_autoencoder():
    code = '''
    # Importing Packages
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import tensorflow as tf
    from sklearn.metrics import accuracy_score, precision_score, recall_score
    from sklearn.model_selection import train_test_split
    from tensorflow.keras import layers, losses,Input
    from tensorflow.keras.layers import Dense
    from tensorflow.keras.datasets import mnist
    from tensorflow.keras.models import Model

    # Loading Data
    (x_train, _), (x_test, _) = mnist.load_data()

    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.

    print (x_train.shape)
    print (x_test.shape)

    # Reshaping Data
    x_train=x_train.reshape((x_train.shape[0],x_train.shape[1]**2))
    x_test=x_test.reshape((x_test.shape[0],x_test.shape[1]**2))

    print (x_train.shape)
    print (x_test.shape)

    # Defining model
    input_image = Input(shape=(784,))
    encoded = Dense(32,activation = "relu")(input_image)
    decoded = Dense(784,activation = "sigmoid")(encoded)

    autoencoder = Model(input_image,decoded)

    # Compiling the model
    autoencoder.compile(optimizer="adam",loss = "binary_crossentropy",metrics = ["mean_squared_error"])

    # Model summary
    autoencoder.summary()

    # Fitting data in the model
    autoencoder.fit(x_train,x_train,epochs = 16,batch_size = 100,validation_data = (x_test,x_test))

    # Predictions using auto encoder
    decoded_images = autoencoder.predict(x_test)

    # Plotting original and feature extracted images
    n = 10
    plt.figure(figsize=(20, 4))
    for i in range(1, n + 1):
        # Display original 
        ax = plt.subplot(2, n, i)
        plt.imshow(x_test[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # Display reconstruction
        ax = plt.subplot(2, n, i + n)
        plt.imshow(decoded_images[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        
    plt.show()
    '''
    print(code)

def get_deep_autoencoder():
    code = '''
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import tensorflow as tf

    from sklearn.metrics import accuracy_score, precision_score, recall_score
    from sklearn.model_selection import train_test_split
    from tensorflow.keras import layers, losses,Input
    from tensorflow.keras.layers import Dense
    from tensorflow.keras.datasets import mnist
    from tensorflow.keras.models import Model

    (x_train, _), (x_test, _) = mnist.load_data()

    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.

    print (x_train.shape)
    print (x_test.shape)

    x_train=x_train.reshape((x_train.shape[0],x_train.shape[1]**2))
    x_test=x_test.reshape((x_test.shape[0],x_test.shape[1]**2))

    print (x_train.shape)
    print (x_test.shape)

    loss_dict = {"adam":0.0,"rmsprop":0.0,"adadelta":0.0,"adagrad":0.0,"nadam":0.0,"sgd":0.0}
    def train_model(input_layer,output_layer,optimizer,epochs,batch_size):
        autoencoder = Model(input_image,decoded)
        autoencoder.compile(optimizer=optimizer,loss = "binary_crossentropy",metrics = ["mean_squared_error"])
    #     print(autoencoder.summary())
        print("With", optimizer,"optimizer")
        hist = autoencoder.fit(x_train,x_train,epochs = epochs,batch_size = batch_size,validation_data = (x_test,x_test))
        loss_dict[optimizer] = hist.history["val_loss"][-1]
        decoded_images = autoencoder.predict(x_test)
        n = 10
        plt.figure(figsize=(20, 4))
        for i in range(1, n + 1):
            # Display original
            ax = plt.subplot(2, n, i)
            plt.imshow(x_test[i].reshape(28, 28))
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            
            # Display reconstruction
            ax = plt.subplot(2, n, i + n)
            plt.imshow(decoded_images[i].reshape(28, 28))
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
        plt.show()
        
    input_image = Input(shape=(784,))
    encoded = Dense(784,activation = "relu")(input_image)
    encoded = Dense(392,activation = "relu")(encoded)
    encoded = Dense(196,activation = "relu")(encoded)
    encoded = Dense(128,activation = "relu")(encoded)
    decoded = Dense(196,activation = "relu")(encoded)
    decoded = Dense(392,activation = "relu")(decoded)
    decoded = Dense(784,activation = "sigmoid")(decoded)

    for i in ["adam","rmsprop","adadelta","adagrad","nadam","sgd"]:
        train_model(input_image,decoded,i,10,32)
    '''
    print(code)

def get_denoising_autoencoder():
    code = '''
    # Importing Packages
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import tensorflow as tf
    from sklearn.metrics import accuracy_score, precision_score, recall_score
    from sklearn.model_selection import train_test_split
    from tensorflow.keras import layers, losses,Input
    from tensorflow.keras.layers import Dense,Conv2D,MaxPooling2D,UpSampling2D
    from tensorflow.keras.datasets import fashion_mnist
    from tensorflow.keras.models import Model
    from math import log10, sqrt

    # Importing Data
    (x_train, _), (x_test, _) = fashion_mnist.load_data()

    # Normalizing Data
    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.

    # Reshaping Data
    x_train=x_train.reshape((x_train.shape[0],x_train.shape[1]**2))
    x_test=x_test.reshape((x_test.shape[0],x_test.shape[1]**2))

    # Applying noise to the image
    noise_factor = 0.4
    x_train_noisy = x_train + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_train.shape) 
    x_test_noisy = x_test + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_test.shape)

    # Clipping the values to 0 and 1 after applying noise
    x_train_noisy = np.clip(x_train_noisy, 0., 1.)
    x_test_noisy = np.clip(x_test_noisy, 0., 1.)

    # Visualizing images with noise
    n = 10
    plt.figure(figsize=(20, 2))
    for i in range(1, n + 1):
        ax = plt.subplot(1, n, i)
        plt.imshow(x_test_noisy[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()

    # Function for finding PSNR Value
    def PSNR(original, compressed):
        mse = np.mean((original - compressed) ** 2)
        if(mse == 0):
            return 100
        max_pixel = 255.0
        psnr = 20 * log10(max_pixel / sqrt(mse))
        return psnr

    # Saving losss values 
    loss_dict = {"adam":0.0,"rmsprop":0.0,"adadelta":0.0,"adagrad":0.0,"nadam":0.0,"sgd":0.0}

    # Function to train model
    def train_model(factor,input_layer,output_layer,optimizer,epochs,batch_size):
        noise_factor = factor
        x_train_noisy = x_train + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_train.shape) 
        x_test_noisy = x_test + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_test.shape) 

        x_train_noisy = np.clip(x_train_noisy, 0., 1.)
        x_test_noisy = np.clip(x_test_noisy, 0., 1.)
        
        autoencoder = Model(input_layer,output_layer)
        autoencoder.compile(optimizer=optimizer,loss = "binary_crossentropy",metrics = ["mean_squared_error"])
        print("With", optimizer,"optimizer, noise factor - ",factor,", epochs - ",epochs,", batch_size - ",batch_size)
        hist = autoencoder.fit(x_train_noisy,x_train,epochs = epochs,batch_size = batch_size,validation_data = (x_test_noisy,x_test))
        loss_dict[optimizer] = hist.history["val_loss"][-1]
        decoded_images = autoencoder.predict(x_test)
        n = 10
        plt.figure(figsize=(20, 4))
        for i in range(1, n + 1):
            # Display original
            ax = plt.subplot(2, n, i)
            plt.imshow(x_test_noisy[i].reshape(28, 28))
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            
            # Display reconstruction
            ax = plt.subplot(2, n, i + n)
            plt.imshow(decoded_images[i].reshape(28, 28))
            plt.gray()
            plt.title(f"PSNR:{round(PSNR(x_test[i],decoded_images[i]),2)}")
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
        plt.show()

    # Input size for the model
    input_size = 784

    # Bottle Neck size
    encoding_size = 128

    # Input Layer
    input_img = Input(shape=(input_size,))
    # Bottleneck layer
    encoded = Dense(encoding_size, activation='relu')(input_img)
    # Output layer
    decoded = Dense(input_size, activation='relu')(encoded)

    # HyperParameter Tuning 
    epochs = [1,10]
    batch_size = [32,64,128]
    for i in ["adam","adadelta"]:
    for j in batch_size:
        for k in epochs:
            train_model(0.4,input_img,decoded,i,k,j)
    '''
    print(code)

def get_sparse_autoencoder():
    code = '''
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import tensorflow as tf

    from sklearn.metrics import accuracy_score, precision_score, recall_score
    from sklearn.model_selection import train_test_split
    from tensorflow.keras import layers, losses,Input
    from tensorflow.keras.layers import Dense,Conv2D,MaxPooling2D,UpSampling2D
    from tensorflow.keras.datasets import mnist
    from tensorflow.keras.models import Model
    from keras import regularizers

    (x_train, _), (x_test, _) = mnist.load_data()

    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.
    x_train=x_train.reshape((x_train.shape[0],x_train.shape[1]**2))
    x_test=x_test.reshape((x_test.shape[0],x_test.shape[1]**2))

    input_img = Input(shape=(784,))
    # Add a Dense layer with a L1 activity regularizer
    encoded = Dense(1024, activation='relu',activity_regularizer=regularizers.l1(10e-5))(input_img)
    decoded = Dense(784, activation='sigmoid')(encoded)

    loss_dict = {"adam":0.0,"rmsprop":0.0,"adadelta":0.0,"adagrad":0.0,"nadam":0.0,"sgd":0.0}
    def train_model(input_layer,output_layer,optimizer,epochs,batch_size):
        autoencoder = Model(input_layer,output_layer)
        autoencoder.compile(optimizer=optimizer,loss = "binary_crossentropy",metrics = ["mean_squared_error"])
    #     print(autoencoder.summary())
        print("With", optimizer,"optimizer")
        hist = autoencoder.fit(x_train_noisy,x_train,epochs = epochs,batch_size = batch_size,validation_data = (x_test_noisy,x_test))
        loss_dict[optimizer] = hist.history["val_loss"][-1]
        decoded_images = autoencoder.predict(x_test)
        n = 10
        plt.figure(figsize=(20, 4))
        for i in range(1, n + 1):
            # Display original
            ax = plt.subplot(2, n, i)
            plt.imshow(x_test[i].reshape(28, 28))
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            
            # Display reconstruction
            ax = plt.subplot(2, n, i + n)
            plt.imshow(decoded_images[i].reshape(28, 28))
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
        plt.show()

    for i in ["adam","rmsprop","adadelta","adagrad","nadam","sgd"]:
            train_model(input_img,decoded,i,10,128)
    '''
    print(code)

def get_cnn_autoencoder():
    code = '''
    import pandas as pd
    import os
    import numpy as np
    import matplotlib.pyplot as plt
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, UpSampling2D,Input
    from tensorflow.keras.callbacks import TensorBoard
    from tensorflow.keras.preprocessing import image
    import keras
    from keras import layers,Model
    from tqdm import tqdm
    from math import log10, sqrt

    train_path = '../input/butterfly-dataset/test/'
    test_path = '../input/butterfly-dataset/train/'
    train = []
    for filename in os.listdir(train_path):
        if filename.endswith('.jpg'):
            img = image.load_img(train_path + filename, target_size=(128, 128))
            img = image.img_to_array(img)
            train.append(img)
    train = np.array(train)

    test = []
    for filename in os.listdir(test_path):
        if filename.endswith('.jpg'):
            img = image.load_img(test_path + filename, target_size=(128, 128))
            img = image.img_to_array(img)
            test.append(img)
    test = np.array(test)

    x_train = train.astype('float32') / 255
    x_test = test.astype('float32') / 255

    def show_data(X, n=10,title=""):
        plt.figure(figsize=(10, 3))
        for i in range(n):
            ax = plt.subplot(2,n,i+1)
            plt.imshow(X[i])
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
        plt.suptitle(title, fontsize = 20)
        
    show_data(x_train,title= "Train Images")
    show_data(x_test,title= "Test Images")

    #Model
    input_img = Input(shape=(128, 128, 3))

    x = Conv2D(128, kernel_size=(3,3), activation="relu", padding = "same")(input_img)
    x = MaxPooling2D(pool_size = (2,2), padding = "same")(x)

    x = Conv2D(64, kernel_size=(3,3), activation="relu", padding = "same")(x)
    encoded = MaxPooling2D(pool_size = (2,2), padding = "same")(x)

    x = Conv2D(64, kernel_size=(3,3), activation="relu", padding = "same")(encoded)
    x = UpSampling2D((2,2))(x)

    x = Conv2D(128, kernel_size=(3,3), activation="relu", padding = "same")(x)
    x = UpSampling2D((2,2))(x)

    decoded = Conv2D(3, kernel_size=(3,3), activation="sigmoid", padding = "same")(x)

    def PSNR(original, compressed):
        mse = np.mean((original - compressed) ** 2)
        if(mse == 0):
            return 100
        max_pixel = 255.0
        psnr = 20 * log10(max_pixel / sqrt(mse))
        return psnr

    loss_dict = {"adam":0.0,"rmsprop":0.0,"adadelta":0.0,"adagrad":0.0,"nadam":0.0,"sgd":0.0}
    def train_model(input_layer,output_layer,optimizer,epochs,batch_size):
        autoencoder = Model(input_layer,output_layer)
        autoencoder.compile(optimizer=optimizer,loss = "binary_crossentropy",metrics = ["mean_squared_error"])
    #     print(autoencoder.summary())
        print("With", optimizer,"optimizer and",epochs,"epochs")
        hist = autoencoder.fit(x_train,x_train,epochs = epochs,batch_size = batch_size,validation_data = (x_test,x_test),verbose = 0)
        loss_dict[optimizer] = hist.history["val_loss"][-1]
        decoded_images = autoencoder.predict(x_test)
        n = 10
        plt.figure(figsize=(20, 4))
        for i in range(1, n + 1):
            # Display original
            plt.suptitle("Original", fontsize = 20)
            ax = plt.subplot(2, n, i)
            plt.imshow(x_test[i].reshape(128,128,3))
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
        plt.show()
        
        plt.figure(figsize=(20,4))
        
        for i in range(1, n + 1):
            # Display reconstruction
            plt.suptitle("Reconstructed", fontsize = 20)
            ax = plt.subplot(2, n, i)
            plt.imshow(decoded_images[i].reshape(128,128,3))
            plt.gray()
            plt.title(f"PSNR:{round(PSNR(x_test[i],decoded_images[i]),2)}")
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
        plt.show()
        
    for i in tqdm(["adam","rmsprop","adadelta","adagrad","nadam","sgd"]):
        for j in [1,50,100,200,300]:
            train_model(input_img,decoded,i,j,4)
    '''
    print(code)