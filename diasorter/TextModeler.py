class TextModeler:
    """Helper class with static methods used for custom string handling"""

    def __new__(cls):
        """instances of TextModeler are forbidden

        Raises:
            TypeError: during instantce making -> forbidden
        """
        raise TypeError(
            "TextModeler is a static class used for holding functions for string editing. It cannot be instanced"
        )

    @staticmethod
    def cleanSpaces(string: str) -> str:
        """Clears spaces before and after the string and multiple following spaces

        Args:
            string (str): original string

        Returns:
            str: spaces cleaned string
        """
        if not isinstance(string, str):
            return string
        return " ".join(string.split())
