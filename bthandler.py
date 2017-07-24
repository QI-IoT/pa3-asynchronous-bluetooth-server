import asyncore
import logging
from bterror import BTError

logger = logging.getLogger(__name__)


class BTClientHandler(asyncore.dispatcher_with_send):
    """BT handler for client-side socket"""

    def __init__(self, socket, server):
        asyncore.dispatcher_with_send.__init__(self, socket)
        self._server = server
        self._data = ""

    def handle_read(self):
        try:
            data = self.recv(1024)
            if not data:
                return

            lf_char_index = data.find('\n')

            if lf_char_index == -1:
                # No new line character in data, so we append all.
                self._data += data
            else:
                # We see a new line character in data, so append rest and handle.
                self._data += data[:lf_char_index]
                print "received [%s]" % self._data

                self.send(self._data + '\n')

                # Clear the buffer
                self._data = ""
        except Exception as e:
            BTError.print_error(handler=self, error=BTError.ERR_READ, error_message=repr(e))
            self._data = ""
            self.close()

    def handle_close(self):
        # flush the buffer
        while self.writable():
            self.handle_write()
        self.close()
