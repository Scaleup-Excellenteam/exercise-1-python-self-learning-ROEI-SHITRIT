class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient,message_title ,message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param str message_title: The title of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'unread': True,
            'title': message_title
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self,usernames,n=-1):
        counter = 1
        result = []
        if usernames not in self.boxes.keys():
            return None
        for message_id in self.boxes[usernames]:
            if n==counter:
                break
            if message_id.unread:
                result.append(message_id)
                message_id.unread = False
                counter+=1
        return result



    def search_inbox(self, username, search_string):
        """Search the user's inbox for messages containing the search string
        in the body of the message.

        :param str username: The username whose inbox we are searching.
        :param str search_string: The string to search for in the messages.
        :return: List of matching messages.
        :rtype: list
        """
        if username not in self.boxes:
            return []

        matching_messages = [
            message for message in self.boxes[username]
            if search_string.lower() in message['body'].lower()
        ]

        return matching_messages




