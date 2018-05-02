import pika


credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(host="localhost",
                                       credentials=credentials,
                                       heartbeat_interval=600)


def test_simple_producer_consumer():
    print("Creating Connection, testing simple producer and consumer")

    # Create Connection
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='hello-queue')

    # Publish to Queue
    print("About to publish to queue")
    channel.basic_publish(exchange='', routing_key='hello-queue', body='test')  # publish to default exchange
    print "After Channel Publish"

    # Consume from Queue and run callback
    channel.basic_consume(callback, queue='hello-queue', no_ack=True)  # acknowledge
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    connection.close()


def callback(ch, method, properties, body):
    """ Callback from Consumer """
    print(" [x] Received %r" % body)


if __name__ == '__main__':
    test_simple_producer_consumer()

