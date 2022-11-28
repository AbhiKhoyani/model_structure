'''
train the model on the input data, and evaluate each epoch on the dev set.

python train.py --model_dir experiments/base_model
python evaluate.py --model_dir experiments/base_model


experiments/base_model/params.json

{
"learning_rate": 1e-3,
"batch_size": 32,
"num_epochs": 20
}

'''