from loguru import logger


def retrain():
    # TODO
    # - take the target path
    # - produce a list of directories
    # - ignore directory names starting with underscore as irrelevant
    # - list files in each relevant directory
    # - filter out files we have already trained on
    # - choose {sample-size} number of images for each directory
    # - create a mirror of the directories and images in /tmp, in the dataset format with symlinks
    # - run yolo train on the previous best model
    #
    # run some experiments to check if the iterative method of training converges over N-generations
    # compare that to retraining the base model with the max sample size used by previous experiment
    #
    # update selection process as advised by the experiment results
    #
    # edge case: files get renamed, potentially causing overfitting. use visual hashing
    # edge case: file gets deleted during training. check how yolo deals with that
    logger.info("Starting a retrain")
