import asyncore
import logging
from bterror import BTError

logger = logging.getLogger(__name__)


class BTHandler(asyncore.dispatcher_with_send):
    def __init__(self, socket, server):
        asyncore.dispatcher_with_send.__init__(self, socket)
        self._server = server
        self._recv_buffer = ""
        self._send_buffer = ""

    def handle_read(self):
        try:
            data = self.recv(1024)
            if not data:
                return

            lf_char_index = data.find('\n')

            if lf_char_index == -1:
                # no new line character in data - so we append all
                self._recv_buffer += data
            else:
                # we see a new line character in data - so append rest and handle
                self._recv_buffer += data[:lf_char_index]
                print "received [%s]" % str(self._recv_buffer)

                self._send_buffer = self._recv_buffer + '\n'
                self.handle_write()

                # clear the buffer
                self._recv_buffer = ""
        except Exception as e:
            BTError.print_error(handler=self, error=BTError.ERR_READ, error_message=repr(e))
            self.close()

    def handle_write(self):
        try:
            sent = self.send(self._send_buffer)
            self._send_buffer = self._send_buffer[sent:]
        except Exception as e:
            BTError.print_error(handler=self, error=BTError.ERR_WRITE,error_message=repr(e))
            self.close()