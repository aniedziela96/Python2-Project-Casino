class Track:
    """"
    A class used to represent a track for races.

    :param track_type: A track type
    :type track_type: str
    :param distance: A distance of the track (in meters)
    :type distance: int
    """
    def __init__(self, track_type: str, distance: int) -> None:
        """
        Constructor method.
        """
        self.track_type = track_type
        self.distance = distance

    def __str__(self) -> str:
        return f"The track is {self.track_type} in length {self.distance} m."

    def get_track_type(self) -> str:
        """
        Track type's getter.

        :return: The type of the track
        :rtype: str
        """
        return self.track_type

    def get_distance(self) -> int:
        """
        Distance's getter.

        :return: The distance of the track
        :rtype: int
        """
        return self.distance
