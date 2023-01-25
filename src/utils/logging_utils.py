import logging

loggers= {}
def create_logger(log_level : str = 'INFO', log_name : str = 'log_file', export_log : bool = False, save_dir : str = ''):
    if log_name in loggers.keys():
        logger= loggers.get(log_name)
    else:
        logger= logging.getLogger(log_name)
        logger.setLevel(logging.DEBUG)
        msg_formatter= logging.Formatter('[%(asctime)s] {%(name)s:%(lineno)d} %(levelname)s - %(message)s','%m-%d %H:%M:%S')

        display_handler= logging.StreamHandler()
        display_handler.setLevel(log_level)
        display_handler.setFormatter(msg_formatter)
        logger.addHandler(display_handler)

        if len(save_dir) > 0:
            save_path= f'{save_dir}{log_name}'
        
        if export_log:
            try:
                save_handler= logging.FileHandler(filename= f'{save_path}.log', mode= 'a')
            except:
                open(f'{save_path}.log', mode= 'x')
                save_handler= logging.FileHandler(filename= f'{save_path}.log', mode= 'w')
            save_handler.setLevel(log_level)
            save_handler.setFormatter(msg_formatter)
            logger.addHandler(save_handler)
        loggers[log_name]= logger
    return logger
        