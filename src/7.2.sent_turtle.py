""" A Post Office system that allows users to send, receive, and search messages.

  send_message: Sends a message to a recipient, marking it as urgent if needed.
  read_inbox: Retrieves a specified number of unread messages from a user's inbox.
""" search_inbox: Searches for messages in a user's inbox based on a keyword.

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

    def read_inbox(self,username,n=-1):
        """
        Retrieves a specified number of unread messages from a user's inbox.

        Marks messages as read after retrieval.

        Args:
            username (str): The username whose inbox will be accessed.
            n (int, optional): The maximum number of unread messages to retrieve.
                               Defaults to -1, which means retrieving all unread messages.

        Returns:
            list: A list of unread messages from the user's inbox.
            None: If the username does not exist.

        Example:
            #>>> po.read_inbox("alice", 2)
            [{'id': 1, 'body': 'Hello!', 'sender': 'bob', 'unread': False, 'title': 'Greeting'},
             {'id': 2, 'body': 'How are you?', 'sender': 'bob', 'unread': False, 'title': 'Check-in'}]
        """
        counter = 0
        result = []
        if username not in self.boxes.keys():
            return None
        for message_id in self.boxes[username]:
            if n==counter:
                break
            if message_id['unread']:
                result.append(message_id)
                message_id['unread'] = False
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
              if search_string.lower() in message['body'].lower() or search_string.lower() in message['title'].lower()
        ]

        return matching_messages


