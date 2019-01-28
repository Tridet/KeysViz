import logging

def createLogHandler(job_name,log_file):
	logger = logging.getLogger(job_name)
	## create a file handler ##
	handler = logging.FileHandler(log_file)
	## create a logging format ##
	formatter = logging.Formatter('%(asctime)s ; %(message)s')
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	logger.setLevel(logging.DEBUG)
	return logger

