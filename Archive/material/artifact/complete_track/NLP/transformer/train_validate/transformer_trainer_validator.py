from transformer import transformer_hyperparas
from public import paths
import random
import numpy as np
import torch
from d2l import torch as d2l
import pickle


class TransformerTrainerValidator:
    def __init__(self, seed):
        self.read_file(seed)
        self.optimizer = torch.optim.Adam(self.net.parameters(), lr=0, betas=(0.9, 0.98), eps=1e-9)
        # read optimizer and randomness state (in case continue from the middle of training)
        if self.step > 1:
            self.optimizer.load_state_dict(self.checkpoint_dict['optimizer_state_dict'])
            random.setstate(self.checkpoint_dict['python_random_state'])
            np.random.set_state(self.checkpoint_dict['numpy_random_state'])
            torch.set_rng_state(self.checkpoint_dict['torch_random_state'])
        self.loss = d2l.MaskedSoftmaxCELoss()
        self.net.train()
        self.train(seed)

    def read_file(self, seed):
        self.checkpoint_dict = torch.load(paths.transformer_record_path + str(seed) + '/checkpoint_dict')
        # read model state
        self.device = self.checkpoint_dict['device']
        self.net = self.checkpoint_dict['net_model']
        self.net.load_state_dict(self.checkpoint_dict['net_state_dict'])
        self.net.to(self.device)

        self.max_epochs = self.checkpoint_dict['max_epochs']
        self.epochs_finished = self.checkpoint_dict['epochs_finished']
        self.step = self.checkpoint_dict['step']

        f = open(paths.transformer_record_path + str(seed) + '/data_iter_dict', 'rb')
        data_iter_dict = pickle.load(f)
        f.close()
        self.train_data_iter = data_iter_dict['train']
        self.dev_data_iter = data_iter_dict['dev']

        f = open(paths.preprocess_info_dict_path, 'rb')
        preprocess_info_dict = pickle.load(f)
        f.close()
        self.tgt_vocab = preprocess_info_dict['stl_tokenizer']

    def lrate_compute(self):
        return transformer_hyperparas.factor * transformer_hyperparas.num_hiddens ** (-0.5) * \
               min(self.step ** (-0.5), self.step * transformer_hyperparas.warmup_steps ** (-1.5))

    def train(self, seed):
        while self.epochs_finished < self.max_epochs:
            timer = d2l.Timer()
            metric = d2l.Accumulator(4)  # sum loss in 1 batch, sum acc in 1 batch, batch size, no. valid tokens
            batch_index = 1

            for batch in self.train_data_iter:
                self.optimizer.zero_grad()
                X, X_valid_len, Y, Y_valid_len = [x.to(self.device) for x in batch]
                # use tokenizer
                bos = torch.tensor(self.tgt_vocab.encode('<bos>').ids * Y.shape[0],
                                   device=self.device).reshape(-1, 1)
                dec_input = torch.cat([bos, Y[:, :-1]], 1)  # Teacher forcing
                Y_hat, _ = self.net(X, dec_input, X_valid_len, Y_valid_len)
                l = self.loss(Y_hat, Y, Y_valid_len)
                # l.sum().backward()  # Make the loss scalar for `backward`
                (l.sum() / Y.shape[0]).backward()  # average on batch size
                #d2l.grad_clipping(self.net, 1)
                lrate = self.lrate_compute()
                for p in self.optimizer.param_groups:
                    p['lr'] = lrate
                self.optimizer.step()
                with torch.no_grad():
                    num_tokens = Y_valid_len.sum()
                    acc_sum = self.accuracy_compute(Y_hat, Y)
                    # sum loss in 1 batch, sum acc in 1 batch, batch size, no. valid tokens
                    metric.add(l.sum(), acc_sum, Y.shape[0], num_tokens)
                    # print batch log and write to file
                    batch_log = 'Train, Epoch: {}, Batch: {}, Step num: {}, Learning rate: {:.8f}, Avg batch loss: {:.4f}, Avg batch acc: {:.4f}'.\
                        format(self.epochs_finished+1, batch_index, self.step, lrate, l.sum()/Y.shape[0], acc_sum/Y.shape[0])
                    print(batch_log)
                    self.log_write(batch_log, seed)
                    # add counters
                    batch_index = batch_index + 1
                    self.step = self.step + 1

            # print epoch log and write to file
            time_taken = timer.stop()
            train_loss = metric[0] / metric[2]
            train_acc = metric[1] / metric[2]
            train_speed = metric[3] / time_taken
            epoch_log \
                = 'Train, Epoch: {}, Avg epoch loss: {:.4f}, Avg epoch acc: {:.4f}, Overall time: {:.1f} s, Speed: {:.1f} tokens/s'.\
                format(self.epochs_finished+1, train_loss, train_acc, time_taken, train_speed)
            epoch_log = epoch_log + ' on ' + str(self.device) + '\n'
            print(epoch_log)
            self.log_write(epoch_log, seed)
            # validate
            validate_loss, validate_acc = self.validate(seed)
            # add counters
            self.epochs_finished = self.epochs_finished + 1
            # save and read checkpoint
            self.checkpoint_write_read(train_loss, train_acc, validate_loss, validate_acc, seed)

    def validate(self, seed):
        with torch.no_grad():
            timer = d2l.Timer()
            metric = d2l.Accumulator(4)  # sum loss in 1 batch, sum acc in 1 batch, batch size, no. valid tokens
            batch_index = 1
            for batch in self.dev_data_iter:
                X, X_valid_len, Y, Y_valid_len = [x.to(self.device) for x in batch]
                # use tokenizer
                bos = torch.tensor(self.tgt_vocab.encode('<bos>').ids * Y.shape[0],
                                   device=self.device).reshape(-1, 1)
                dec_input = torch.cat([bos, Y[:, :-1]], 1)  # Teacher forcing
                Y_hat, _ = self.net(X, dec_input, X_valid_len, Y_valid_len)
                l = self.loss(Y_hat, Y, Y_valid_len)
                num_tokens = Y_valid_len.sum()
                acc_sum = self.accuracy_compute(Y_hat, Y)
                # sum loss in 1 batch, sum acc in 1 batch, batch size, no. valid tokens
                metric.add(l.sum(), acc_sum, Y.shape[0], num_tokens)
                # print batch log and write to file
                batch_log = 'Validate, Epoch: {}, Batch: {}, Avg batch loss: {:.4f}, Avg batch acc: {:.4f}'. \
                    format(self.epochs_finished+1, batch_index, l.sum()/Y.shape[0], acc_sum/Y.shape[0])
                print(batch_log)
                self.log_write(batch_log, seed)
                # add counters
                batch_index = batch_index + 1

            # print epoch log and write to file
            time_taken = timer.stop()
            validate_loss = metric[0] / metric[2]
            validate_acc = metric[1] / metric[2]
            validate_speed = metric[3] / time_taken
            epoch_log \
                = 'Validate, Epoch: {}, Avg epoch loss: {:.4f}, Avg epoch acc: {:.4f}, Overall time: {:.1f} s, Speed: {:.1f} tokens/s' \
                .format(self.epochs_finished+1, validate_loss, validate_acc, time_taken,
                        validate_speed)
            epoch_log = epoch_log + ' on ' + str(self.device) + '\n'
            print(epoch_log)
            self.log_write(epoch_log, seed)

        return validate_loss, validate_acc

    def accuracy_compute(self, Y_hat, Y):
        acc_sum = 0
        for i in range(Y.shape[0]):
            prediction = Y_hat[i]    # shape: (len, vocab_size)
            reference_index = Y[i]  # shape: (len,)
            prediction_index = prediction.argmax(dim=1)

            prediction_list = prediction_index.cpu().numpy().tolist()
            reference_list = reference_index.cpu().numpy().tolist()
            eos_id = self.tgt_vocab.encode('<eos>').ids[0]
            id_last = reference_list.index(eos_id)
            del reference_list[id_last:]
            del prediction_list[id_last:]
            if len(reference_list) != len(prediction_list):
                print('Error!')

            prediction_tensor_new = torch.tensor(prediction_list)
            reference_tensor_new = torch.tensor(reference_list)
            correct_list, correct_num = self.correct_num_compute(prediction_tensor_new, reference_tensor_new)
            total_number = prediction_tensor_new.shape[0]
            sample_acc = correct_num / total_number
            acc_sum = acc_sum + sample_acc

            if i == Y.shape[0] - 1:
                print()
                print('Last sample in batch:')
                print('prediction id:')
                print(prediction_list)
                print('reference id:')
                print(reference_list)
                print('correctness:')
                print(correct_list)

                prediction_str = self.tgt_vocab.decode(prediction_list, skip_special_tokens=False)
                reference_str = self.tgt_vocab.decode(reference_list, skip_special_tokens=False)
                print('prediction:', prediction_str)
                print('reference: ', reference_str)
                print('acc:', sample_acc)

        return acc_sum

    @staticmethod
    def correct_num_compute(y_hat, y):
        cmp = y_hat.type(y.dtype) == y
        return cmp.type(y.dtype).cpu().numpy().tolist(), float(cmp.type(y.dtype).sum())

    @staticmethod
    def log_write(log, seed):
        with open(paths.transformer_record_path + str(seed) + '/log.txt', 'a') as f:
            f.write(log + '\n')

    def checkpoint_write_read(self, train_loss, train_acc, validate_loss, validate_acc, seed):
        # write checkpoint dict to file
        self.checkpoint_dict['net_state_dict'] = self.net.state_dict()
        self.checkpoint_dict['optimizer_state_dict'] = self.optimizer.state_dict()
        self.checkpoint_dict['epochs_finished'] = self.epochs_finished
        self.checkpoint_dict['step'] = self.step  # this is the index of next step
        self.checkpoint_dict['train_loss_list'].append(train_loss)
        self.checkpoint_dict['train_acc_list'].append(train_acc)
        self.checkpoint_dict['validate_loss_list'].append(validate_loss)
        self.checkpoint_dict['validate_acc_list'].append(validate_acc)
        # save randomness state for python, numpy, torch
        self.checkpoint_dict['python_random_state'] = random.getstate()
        self.checkpoint_dict['numpy_random_state'] = np.random.get_state()
        self.checkpoint_dict['torch_random_state'] = torch.get_rng_state()
        torch.save(self.checkpoint_dict, paths.transformer_record_path + str(seed) + '/checkpoint_dict')
        torch.save(self.checkpoint_dict['net_state_dict'], paths.transformer_record_path + str(seed) + '/net_state_dict')
        info_dict = {
            'step': self.checkpoint_dict['step'] - 1,  # this is the index of current step
            'train_loss_list': self.checkpoint_dict['train_loss_list'],
            'train_acc_list': self.checkpoint_dict['train_acc_list'],
            'validate_loss_list': self.checkpoint_dict['validate_loss_list'],
            'validate_acc_list': self.checkpoint_dict['validate_acc_list']
        }
        torch.save(info_dict, paths.transformer_record_path + str(seed) + '/info_dict')
        # read checkpoint dict
        self.checkpoint_dict = torch.load(paths.transformer_record_path + str(seed) + '/checkpoint_dict')
        # read states model and optimizer
        self.net.load_state_dict(self.checkpoint_dict['net_state_dict'])
        self.optimizer.load_state_dict(self.checkpoint_dict['optimizer_state_dict'])
        # read randomness states
        random.setstate(self.checkpoint_dict['python_random_state'])
        np.random.set_state(self.checkpoint_dict['numpy_random_state'])
        torch.set_rng_state(self.checkpoint_dict['torch_random_state'])
