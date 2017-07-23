class BTError(object):
    ERR_UNKNOWN = -1
    ERR_NO_CMD = -2
    ERR_UNKNOWN_CMD = -3
    ERR_READ = -4
    ERR_WRITE = -5

    ERROR_MSG = {
        ERR_UNKNOWN:    "Unknown error",
        ERR_NO_CMD:     "No command given",
        ERR_UNKNOWN_CMD:   "Unknown command"
    }

    @staticmethod
    def print_error(handler, error=-1, error_message=""):
        if len(error_message) < 1:
            error_message = BTError.ERROR_MSG[error]

        print "Error %d: %s" % (error, error_message)
        #handler.send_error(error_code=error, error_message=error_message)
