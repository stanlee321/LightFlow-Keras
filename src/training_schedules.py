LONG_SCHEDULE = {
    'step_values': [5000, 25000, 50000, 60000, 70000 ],
    'learning_rates': [0.1, 0.01, 0.01/2, (0.01/2)/2, ((0.01/2)/2)/2, (((0.01/2)/2)/2)/2],
    'momentum': 0.9,
    'momentum2': 0.999,
    'weight_decay': 0.0004,
    'max_iter':75000,
}


FINETUNE_SCHEDULE = {
    # TODO: Finetune schedule
}