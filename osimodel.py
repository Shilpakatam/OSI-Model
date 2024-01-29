class ApplicationLayer:
    def send_text(self, text):
        print("Application Layer: Sending text", text)
        return text

    def receive_text(self, text):
        print("Application Layer: Received text", text)


class PresentationLayer:
    def encode_text(self, text):
        print("Presentation Layer: Encoding text")
        return text.encode('utf-8')

    def decode_text(self, encoded_text):
        print("Presentation Layer: Decoding text")
        return encoded_text.decode('utf-8')


class SessionLayer:
    def establish_session(self, encoded_text):
        print("Session Layer: Establishing session")
        return encoded_text

    def terminate_session(self, text):
        print("Session Layer: Terminating session")


class TransportLayer:
    def segment_text(self, session_text):
        print("Transport Layer: Segmenting text")
        return session_text

    def reassemble_text(self, segmented_text):
        print("Transport Layer: Assembling text")
        return segmented_text


class NetworkLayer:
    def route_text(self, segmented_text):
        print("Network Layer: Routing text")
        return segmented_text


class DataLinkLayer:
    def frame_text(self, routed_text):
        print("Data Link Layer: Framing text")
        return routed_text

    def deframe_text(self, framed_text):
        print("Data Link Layer: Deframing text")
        return framed_text


class PhysicalLayer:
    def send_bits(self, framed_text):
        print("Physical Layer: Sending bits", framed_text)
        return framed_text

    def receive_bits(self, sent_bits):
        print("Physical Layer: Receiving bits", sent_bits)


def main():
    main_text = "'OSI Network Model'"
    application_layer = ApplicationLayer()
    sent_text = application_layer.send_text(main_text)
    presentation_layer = PresentationLayer()
    encoded_text = presentation_layer.encode_text(sent_text)
    session_layer = SessionLayer()
    session_text = session_layer.establish_session(encoded_text)
    transport_layer = TransportLayer()
    segmented_text = transport_layer.segment_text(session_text)
    network_layer = NetworkLayer()
    routed_text = network_layer.route_text(segmented_text)
    datalink_layer = DataLinkLayer()
    framed_text = datalink_layer.frame_text(routed_text)
    physical_layer = PhysicalLayer()
    sent_bits = physical_layer.send_bits(framed_text)
    received_bits = sent_bits
    physical_layer.receive_bits(received_bits)
    received_framed_text = datalink_layer.deframe_text(received_bits)
    received_routed_text = network_layer.route_text(received_framed_text)
    received_segmented_text = transport_layer.reassemble_text(received_routed_text)
    session_layer.terminate_session(received_segmented_text)
    decoded_text = presentation_layer.decode_text(received_segmented_text)
    application_layer.receive_text(decoded_text)

if __name__ == "__main__":
    main()



