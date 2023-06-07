class Track:
    def __init__(self, track_type: str, distance: int):
        self.track_type = track_type
        self.distance = distance

    def __str__(self):
        return f"The track is {self.track_type} in length {self.distance} m."

    def get_track_type(self) -> str:
        return self.track_type

    def get_distance(self) -> int:
        return self.distance
