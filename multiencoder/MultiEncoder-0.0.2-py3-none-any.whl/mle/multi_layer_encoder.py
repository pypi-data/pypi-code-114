from transformers import AutoTokenizer, AutoModel
import numpy as np
import torch
import torch.nn.functional as F


class multi_layer_encoder():
    def __init__(self, model_dir):
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
        self.model = AutoModel.from_pretrained(model_dir, output_hidden_states=True)

        if torch.cuda.is_available():
            device = torch.device("cuda")
            print(f'There are {torch.cuda.device_count()} GPU(s) available.')
            print('Device name:', torch.cuda.get_device_name(0))

        else:
            print('No GPU available, using the CPU instead.')
            device = torch.device("cpu")

        # Helper: Mean and Max Pooling - Take attention mask into account for correct averaging

    def mean_pooling(self,model_output, attention_mask):
        """
        Take the mean of the token embeddings.
        :param model_output:
        :param attention_mask:
        :return: mean pooled embedding
        :rtype: torch.tensor
        """
        token_embeddings = model_output  # First element of model_output contains all token embeddings (last hidden state)
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


        # Max Pooling - Take the max value over time for every dimension.

    def max_pooling(self,model_output, attention_mask):
        """
        Take the max of the token embeddings.
        :param model_output:
        :param attention_mask:
        :return: max pooled embedding
        :rtype: torch.tensor
        """
        token_embeddings = model_output  # First element of model_output contains all token embeddings
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        token_embeddings[input_mask_expanded == 0] = -1e9  # Set padding tokens to large negative value
        return torch.max(token_embeddings, 1)[0]


    def return_last_six_hidden(self,tensor_list, cut_point):
        length_of_tensor_list = len(tensor_list)
        cut_off_point = cut_point  # 6

        dict_of_layer_outputs = {}

        # 6th layer is index 5, don't ask why !
        # 13th layer is index 12, don't ask why ! (aka. last hidden state)
        for i in range(cut_off_point - 1, length_of_tensor_list):
            layer_outputs = tensor_list[i]
            dict_of_layer_outputs[f"layer_{i + 1}"] = layer_outputs

        return dict_of_layer_outputs

    def get_encoded_longformer_input(self,text):
        """
          Encode a text with the longformer model.
          :param text: input text
          :return:
          """
        sentence = text
        encoded_input = self.tokenizer(sentence, padding=True, truncation=True, return_tensors='pt')
        # Compute token embeddings
        with torch.no_grad():
            model_output = self.model(**encoded_input)
        return model_output, encoded_input



    def multi_encode(self, input_text, encode_layers=6, max_pool=False):
         """
         Encode a text with the longformer model.
         :param input_text: The text to encode.
         :param encode_layers: which layers to get encoding from. (From layer 12 to encode_layers)
         :param max_pool: boolean, if true, use max pooling, else use mean pooling
         :return: list of encoded input. The first is the lowest layer, the last is the highest layer.
         :return: dictonary, with keys being the layer name and values being the encoded input.
         :rtype: list, dict
         """
         model_output, encoded_input = self.get_encoded_longformer_input(input_text)
         dect = self.return_last_six_hidden(model_output.hidden_states, encode_layers)

         list_of_encoded_inputs = []  # starts from encoder_layers to last year 12 in the model.

         for key in dect.keys():
             #print("Pooling :", key)  # Take this away!
             if max_pool:
                 sentence_embeddings = self.max_pooling(dect.get(key), encoded_input['attention_mask'])

             else:
                 sentence_embeddings = self.mean_pooling(dect.get(key), encoded_input['attention_mask'])

             list_of_encoded_inputs.append(sentence_embeddings.numpy())

         #print("CAUTION: Dictionary embeddings are not pooled and is of type torch.tensor")
         return list_of_encoded_inputs, dect
