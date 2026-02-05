import networkx as nx

class ScamNetwork:
    def __init__(self):
        self.graph = nx.Graph()

    def add_iocs(self, iocs: dict):
        for acc in iocs["bank_accounts"]:
            self.graph.add_node(acc, type="BANK")

        for ifsc in iocs["ifsc_codes"]:
            self.graph.add_node(ifsc, type="IFSC")

        for upi in iocs["upi_ids"]:
            self.graph.add_node(upi, type="UPI")

        for url in iocs["phishing_urls"]:
            self.graph.add_node(url, type="URL")

        for phone in iocs["phone_numbers"]:
            self.graph.add_node(phone, type="PHONE")

        for acc in iocs["bank_accounts"]:
            for ifsc in iocs["ifsc_codes"]:
                self.graph.add_edge(acc, ifsc)
            for phone in iocs["phone_numbers"]:
                self.graph.add_edge(acc, phone)

        for upi in iocs["upi_ids"]:
            for url in iocs["phishing_urls"]:
                self.graph.add_edge(upi, url)
