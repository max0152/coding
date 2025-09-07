class Packet:
    def __init__(self, src, dst, data):
        self.src = src
        self.dst = dst
        self.data = data


class Computer:
    def __init__(self, name, router):
        self.name = name
        self.router = router

    def send(self, dst, data):
        packet = Packet(self.name, dst, data)
        self.router.route(packet)

    def receive(self, packet):
        print(f"Message for {self.name} from {packet.src}: {packet.data}")


class Router:
    def __init__(self):
        self.devices = {}

    def connect(self, device):
        self.devices[device.name] = device

    def route(self, packet):
        if packet.dst in self.devices:
            self.devices[packet.dst].receive(packet)
        else:
            print(f"Router: destination {packet.dst} not found.")
router = Router()

pc1 = Computer("PC1", router)
pc2 = Computer("PC2", router)
pc3 = Computer("PC3", router)
pc4 = Computer("PC4", router)

router.connect(pc1)
router.connect(pc2)
router.connect(pc3)
router.connect(pc4)
