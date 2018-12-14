class MyMessageProvider:

    def create(self, mention, max_message_length):
        """
        Create a message
        :param mention: JSON object containing mention details from Twitter
        :param max_message_length: Maximum allowable length for created message
        :return: a message
        """
        return "Donkeys here!"

    def dynamicallyGenerateTweet(self, mention, max_message_length):
    	print("What do you want to tweet?")
