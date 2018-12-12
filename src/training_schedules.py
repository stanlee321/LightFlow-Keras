LONG_SCHEDULE = {
    'step_values': [5000, 5600, 13000, 28000, 50000, 60000 ],
    'learning_rates': [0.1, 0.001, 0.00001, 0.001/2, (0.001/2)/2, ((0.001/2)/2)/2, (((0.001/2)/2)/2)/2],
    'momentum': 0.9,
    'momentum2': 0.999,
    'weight_decay': 0.0004,
    'max_iter':75000,
}


FINETUNE_SCHEDULE = {
    # TODO: Finetune schedule
}