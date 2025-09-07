class Packet:
    def __init__(self, src, dst, data):
        self.src = src
        self.dst = dst
        self.data = data


class Computer:
    def __init__(self, mac, router):
        self.mac = mac
        self.router = router

    def send(self, dst, data):
        packet = Packet(self.mac, dst, data)
        self.router.route(packet)

    def receive(self, packet):
        print(f"Message for {self.mac} from {packet.src}: {packet.data}")


class Router:
    BROADCAST_MAC = "FF:FF:FF:FF:FF:FF"
    def __init__(self):
        self.devices = {}

    def connect(self, device):
        self.devices[device.mac] = device

    def route(self, packet):
        if packet.dst in self.devices:
            self.devices[packet.dst].receive(packet)
        else:
            print(f"Router: destination {packet.dst} not found.")
router = Router()

pc1 = Computer("00:11:22:33:44:55", router)
pc2 = Computer("66:77:88:99:AA:BB", router)
pc3 = Computer("CC:DD:EE:FF:00:11", router)
pc4 = Computer("22:33:44:55:66:77", router)

router.connect(pc1)
router.connect(pc2)

pc1.send("CC:DD:EE:FF:00:11", "Привет от PC1!")
pc3.send("00:11:22:33:44:55", "Ответ от PC3!")
pc2.send("22:33:44:55:66:77", "PC2 здесь.")
pc4.send("66:77:88:99:AA:BB", "Принято!")
router.connect(pc3)
router.connect(pc4)
pc1.send(Router.BROADCAST_MAC, "Всем привет от PC1!")
