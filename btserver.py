import asyncore
import logging
from bluetooth import *
from bthandler import BTHandler

logger = logging.getLogger(__name__)


class BTServer(asyncore.dispatcher):
    """Asynchronous Bluetooth  Server"""

    def __init__(self, uuid, service_name, port=PORT_ANY):
        asyncore.dispatcher.__init__(self)

        self._cmds = {}

        if not is_valid_uuid(uuid):
            raise ValueError("uuid %s is not valid" % uuid)

        self.uuid = uuid
        self.service_name = service_name
        self.port = port

        # Create BT socket
        self.set_socket(BluetoothSocket(RFCOMM))
        self.bind(("", port))
        self.listen(1)

        advertise_service(self.socket,
                          service_name,
                          service_id=uuid,
                          service_classes=[uuid, SERIAL_PORT_CLASS],
                          profiles=[SERIAL_PORT_PROFILE]
                          )

        self.port = self.socket.getsockname()[1]
        logger.info("Waiting for connection on RFCOMM channel %d" % self.port)
        print "Waiting for connection on RFCOMM channel %d" % self.port

    def handle_accept(self):
        pair = self.socket.accept()

        if pair is not None:
            sock, addr = pair
            logger.info("Accepted connection from %s" % repr(addr[0]))
            print "Accepted connection from %s" % repr(addr[0])
            handler = BTHandler(socket=sock, server=self)

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

if __name__ == '__main__':
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    service_name = "AsynchronousBTServer"

    server = BTServer(uuid, service_name)
    asyncore.loop()
