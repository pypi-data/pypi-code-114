"""
Author : SHIVAM CHHETRY
19-03-2022

Custome keras callbacks that will control the learning rate and print
training data in spreadsheet format. The callback also includes a feature to
preiodically ask if you want to train for N more epochs or halt.
"""
from tensorflow import keras
import tensorflow as tf
import numpy as np
import time

# Define a function to print text in RGB foreground and background colors

def Print_msg_in_color(txt_msg, fore_tupple, back_tupple):
    """
    Prints the text_msg in the foreground color specified by fore_tupple with the background specified by back_tupple

    :param txt_msg: text_msg is the text that will be shown to the user
    :param fore_tupple  Fore_tupple is foreground color tupple (r, g, b)
    :param back_tupple: Back_tupple is background tupple (r, g, b)
    """

    rf, gf, bf = fore_tupple
    rb, gb, bb = back_tupple
    msg = '{0}' + txt_msg
    mat = '\33[38;2;' + str(rf) + ';' + str(gf) + ';' + str(bf) + ';48;2' + str(rb) + ';' + str(gb) + ';' + str(
        bb) + 'm'
    print(msg, format(mat), flush=True)
    print('\33[0m', flush=True)  # returns default print color to back to back
    return


class ALRCallback(keras.callbacks.Callback):
    def __init__(self,
               model,
               base_model,
               patience,
               stop_patience,
               threshold,
               factor,
               nspace,
               batches,
               initial_epoch,
               epochs,
               ask_epoch
               ):
        """
        :param model: model is the name of your compiled model
        :param base_model:  base_model is the name of the base_model used for transfer learning. If not doing transfer learning set base_model=None
        :param patience:    patience is an integer. This callback initially monitors the training accuracy. If the training accuracy fails to improve
after patience number of epochs the learning rate is reduced where new_lr=old_lr * factor.
The training accuracy is monitored until it achieves or exceeds the float value threshold.
At that point the callback now monitors validation loss.
If the validation loss fails to decrease for patience number of epochs the learning rate is adjusted.
The callback always saves the weights for the epoch with the lowest validation loss.
At the conclusion of training the best weights are loaded into the model.
        :param stop_patience:   stop_patience is an integer. If stop_patience number of consecutive epochs occur where the learning rate was reduced
but the metric being monitored idi not improve the training is halted.
        :param threshold:   threshold is a float between 0 and 1.0. It is the level the training accuracy must meet or exceed for the callback to
switch to monitoring validation loss.
        :param factor:  factor is a float between 0 and 1.0. It determines the new learning rate by the formula new_lr=old_lr * factor
        :param settled:   settled means (
live in or at a specified place) is a boolean. When dwell=True the callback monitors the metric. If the metric fails to improve on the current epoch
it means you have moved to a point in Nspace(N is the number of trainable parameters of the model) that is NOT as good in
terms of the metric value as was the point for the epoch with the best metric performance. So the callback loads the
model with the weights from that epoch. It then reduces the learning rate and continues training. If dwell=False the
scenario described does not occur. However your model always ends up with the weights for the epoch with the best metric
performance laded in the model.
        :param batches: batches is an integer used only for printing purposes. It's value should be the same as train_steps, that is calculated as
batches = number of training samples//batch_size +1. For example if you have 1001 samples and your batch_size is 10
then batches= 10 + 1 = 11.
        :param initial_epoch:   initial_epoch is an integer. Typically set this to zero Itis used in the information printed out for each epoch. In the case where you train the model say with the basemodel weights frozen say you train for 10 epochs. Then you want to fine tune the model and train for more eppochs for the second training session you would reinstantiate the callback and set initial_epoch=10.
        :param epochs:  epochs is an integer and is the value of epochs you use for model.fit
        :param ask_epoch:   ask_epoch is an integer. Lets say it is set to a value N. After the model trains for N epochs the user is queired to provide
input. If an integer is entered say M then training will continue for M more epochs and at the end of epoch M + N the
user is queried again. If the user enters another integer the process continues until epochs number of epochs is run.
If the user is doing transfer learning whene the vale of base_model is NOT None at the query you can enter a T. This will
make the base_model trainable. After entering T you will be queried to enter an integer for how many more epochs to run
before you are queried again. At any query you have the option to enter H to halt training.
        """

        super(ALRCallback, self).__init__()
        self.model = model
        self.base_model = base_model
        self.patience = patience  # specifies how many epochs without improvement before learning rate is adjusted
        self.stop_patience = stop_patience  # specifies how many times to adjust lr without improvement to stop training
        self.threshold = threshold  # specifies training accuracy threshold when lr will be adjusted based on validation loss
        self.factor = factor  # factor by which to reduce the learning rate
        self.nspace = nspace
        self.batches = batches  # number of training batch to runn per epoch
        self.initial_epoch = initial_epoch
        self.epochs = epochs
        self.ask_epoch = ask_epoch
        self.ask_epoch_initial = ask_epoch  # save this value to restore if restarting training
        # callback variables
        self.count = 0  # how many times lr has been reduced without improvement
        self.stop_count = 0
        self.best_epoch = 1  # epoch with the lowest loss
        self.initial_lr = float(
            tf.keras.backend.get_value(model.optimizer.lr))  # get the initiallearning rate and save it
        self.highest_tracc = 0.0  # set highest training accuracy to 0 initially
        self.lowest_vloss = np.inf  # set lowest validation loss to infinity initially
        self.best_weights = self.model.get_weights()  # set best weights to model's initial weights
        self.initial_weights = self.model.get_weights()  # save initial weights if they have to get restored

    def on_train_begin(self, logs=None):
        if self.base_model != None:
            status = self.base_model.trainable
            if status:
                msg = ' initializing callback starting training with base_model trainable'
            else:
                msg = 'initializing callback starting training with base_model not trainable'
        else:
            msg = 'initialing callback and starting training'
        Print_msg_in_color(msg, (244, 252, 3), (55, 65, 80))
        msg = '{0:^8s}{1:^10s}{2:^9s}{3:^9s}{4:^9s}{5:^9s}{6:^9s}{7:^10s}{8:10s}{9:^8s}'.format('Epoch', 'Loss',
                                                                                                'Accuracy',
                                                                                                'V_loss', 'V_acc', 'LR',
                                                                                                'Next LR', 'Monitor',
                                                                                                '% Improv', 'Duration')
        Print_msg_in_color(msg, (244, 252, 3), (55, 65, 80))
        self.start_time = time.time()

    def on_train_end(self, logs=None):
        stop_time = time.time()
        tr_duration = stop_time - self.start_time
        hours = tr_duration // 3600
        minutes = (tr_duration - (hours * 3600)) // 60
        seconds = tr_duration - ((hours * 3600) + (minutes * 60))

        self.model.set_weights(self.best_weights)  # set the weights of the model to the best weights
        msg = f'Training is completed - model is set with weights from epoch {self.best_epoch} '
        Print_msg_in_color(msg, (0, 255, 0), (55, 65, 80))
        msg = f'training elapsed time was {str(hours)} hours, {minutes:4.1f} minutes, {seconds:4.2f} seconds)'
        Print_msg_in_color(msg, (0, 255, 0), (55, 65, 80))

    def on_train_batch_end(self, batch, logs=None):
        acc = logs.get('accuracy') * 100  # get training accuracy
        loss = logs.get('loss')
        msg = '{0:20s}processing batch {1:4s} of {2:5s} accuracy= {3:8.3f}  loss: {4:8.5f}'.format(' ', str(batch),
                                                                                                   str(self.batches),
                                                                                                   acc, loss)
        print(msg, '\r', end='')  # prints over on the same line to show running batch count

    def on_epoch_begin(self, epoch, logs=None):
        self.now = time.time()

    def on_epoch_end(self, epoch, logs=None):  # method runs on the end of each epoch
        later = time.time()
        duration = later - self.now
        lr = float(tf.keras.backend.get_value(self.model.optimizer.lr))  # get the current learning rate
        current_lr = lr
        v_loss = logs.get('val_loss')  # get the validation loss for this epoch
        acc = logs.get('accuracy')  # get training accuracy
        v_acc = logs.get('val_accuracy')
        loss = logs.get('loss')
        if acc < self.threshold:  # if training accuracy is below threshold adjust lr based on training accuracy
            monitor = 'accuracy'
            if epoch == 0:
                pimprov = 0.0
            else:
                pimprov = (acc - self.highest_tracc) * 100 / self.highest_tracc
            if acc > self.highest_tracc:  # training accuracy improved in the epoch
                self.highest_tracc = acc  # set new highest training accuracy
                self.best_weights = self.model.get_weights()  # traing accuracy improved so save the weights
                self.count = 0  # set count to 0 since training accuracy improved
                self.stop_count = 0  # set stop counter to 0
                if v_loss < self.lowest_vloss:
                    self.lowest_vloss = v_loss
                color = (0, 255, 0)
                self.best_epoch = epoch + 1  # set the value of best epoch for this epoch
            else:
                # training accuracy did not improve check if this has happened for patience number of epochs
                # if so adjust learning rate
                if self.count >= self.patience - 1:  # lr should be adjusted
                    color = (245, 170, 66)
                    lr = lr * self.factor  # adjust the learning by factor
                    tf.keras.backend.set_value(self.model.optimizer.lr, lr)  # set the learning rate in the optimizer
                    self.count = 0  # reset the count to 0
                    self.stop_count = self.stop_count + 1  # count the number of consecutive lr adjustments
                    self.count = 0  # reset counter
                    if self.nspace:
                        self.model.set_weights(
                            self.best_weights)  # return to better point in N space
                    else:
                        if v_loss < self.lowest_vloss:
                            self.lowest_vloss = v_loss
                else:
                    self.count = self.count + 1  # increment patience counter
        else:  # training accuracy is above threshold so adjust learning rate based on validation loss
            monitor = 'val_loss'
            if epoch == 0:
                pimprov = 0.0
            else:
                pimprov = (self.lowest_vloss - v_loss) * 100 / self.lowest_vloss
            if v_loss < self.lowest_vloss:  # check if the validation loss improved
                self.lowest_vloss = v_loss  # replace lowest validation loss with new validation loss
                self.best_weights = self.model.get_weights()  # validation loss improved so save the weights
                self.count = 0  # reset count since validation loss improved
                self.stop_count = 0
                color = (0, 255, 0)
                self.best_epoch = epoch + 1  # set the value of the best epoch to this epoch
            else:  # validation loss did not improve
                if self.count >= self.patience - 1:  # need to adjust lr
                    color = (245, 170, 66)
                    lr = lr * self.factor  # adjust the learning rate
                    self.stop_count = self.stop_count + 1  # increment stop counter because lr was adjusted
                    self.count = 0  # reset counter
                    tf.keras.backend.set_value(self.model.optimizer.lr, lr)  # set the learning rate in the optimizer
                    if self.nspace:
                        self.model.set_weights(self.best_weights)  # return to better point in N space
                else:
                    self.count = self.count + 1  # increment the patience counter
                if acc > self.highest_tracc:
                    self.highest_tracc = acc
        msg = f'{str(epoch + 1):^3s}/{str(self.epochs):4s} {loss:^9.3f}{acc * 100:^9.3f}{v_loss:^9.5f}{v_acc * 100:^9.3f}{current_lr:^9.5f}{lr:^9.5f}{monitor:^11s}{pimprov:^10.2f}{duration:^8.2f}'
        Print_msg_in_color(msg, color, (55, 65, 80))
        if self.stop_count > self.stop_patience - 1:  # check if learning rate has been adjusted stop_count times with no improvement
            msg = f' training has been halted at epoch {epoch + 1} after {self.stop_patience} adjustments of learning rate with no improvement'
            Print_msg_in_color(msg, (0, 255, 255), (55, 65, 80))
            self.model.stop_training = True  # stop training
        else:
            if self.ask_epoch != None:
                if epoch + 1 >= self.ask_epoch:
                    if self.base_model.trainable:
                        msg = 'enter H to halt training or an integer for number of epochs to run then ask again'
                    else:
                        msg = 'enter H to halt training ,F to fine tune model, or an integer for number of epochs to run then ask again'
                    Print_msg_in_color(msg, (0, 255, 255), (55, 65, 80))
                    ans = input('')
                    if ans == 'H' or ans == 'h':
                        msg = f'training has been halted at epoch {epoch + 1} due to user input'
                        Print_msg_in_color(msg, (0, 255, 255), (55, 65, 80))
                        self.model.stop_training = True  # stop training
                    elif ans == 'F' or ans == 'f':
                        if self.base_model.trainable:
                            msg = 'base_model is already set as trainable'
                        else:
                            msg = 'setting base_model as trainable for fine tuning of model'
                            self.base_model.trainable = True
                        Print_msg_in_color(msg, (0, 255, 255), (55, 65, 80))
                        msg = '{0:^8s}{1:^10s}{2:^9s}{3:^9s}{4:^9s}{5:^9s}{6:^9s}{7:^10s}{8:^8s}'.format('Epoch',
                                                                                                         'Loss',
                                                                                                         'Accuracy',
                                                                                                         'V_loss',
                                                                                                         'V_acc', 'LR',
                                                                                                         'Next LR',
                                                                                                         'Monitor',
                                                                                                         '% Improv',
                                                                                                         'Duration')
                        Print_msg_in_color(msg, (244, 252, 3), (55, 65, 80))
                        self.count = 0
                        self.stop_count = 0
                        self.ask_epoch = epoch + 1 + self.ask_epoch_initial

                    else:
                        ans = int(ans)
                        self.ask_epoch += ans
                        msg = f' training will continue until epoch ' + str(self.ask_epoch)
                        Print_msg_in_color(msg, (0, 255, 255), (55, 65, 80))
                        msg = '{0:^8s}{1:^10s}{2:^9s}{3:^9s}{4:^9s}{5:^9s}{6:^9s}{7:^10s}{8:10s}{9:^8s}'.format('Epoch',
                                                                                                                'Loss',
                                                                                                                'Accuracy',
                                                                                                                'V_loss',
                                                                                                                'V_acc',
                                                                                                                'LR',
                                                                                                                'Next LR',
                                                                                                                'Monitor',
                                                                                                                '% Improv',
                                                                                                                'Duration')
                        Print_msg_in_color(msg, (244, 252, 3), (55, 65, 80))