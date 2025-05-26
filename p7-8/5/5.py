from datetime import datetime, timedelta

class Lecture:
    def __init__(self, topic: str, start_time: str, duration: str):
        self.topic = topic
        self.start_time = datetime.strptime(start_time, '%H:%M')
        self.duration = self._strptime_to_delta(duration)
        self.end_time = self.start_time + self.duration

    def _strptime_to_delta(self, time: str):
        hours, minutes = map(int, time.split(':'))
        return timedelta(hours=hours, minutes=minutes)

class Conference:
    def __init__(self):
        self.lectures: list[Lecture] = []
        self._total_duration = timedelta(0)

    def _time_range(self, start_time: float|int, end_time: float|int) -> range:
        return range(int(start_time), int(end_time))

    def add(self, new_lecture: Lecture):
        for lecture in self.lectures:
            for minute in self._time_range(new_lecture.start_time.timestamp(), new_lecture.end_time.timestamp()):
                if minute in self._time_range(lecture.start_time.timestamp(), lecture.end_time.timestamp()):
                    raise ValueError('Провести выступление в это время невозможно')
        self.lectures.append(new_lecture)
        self._total_duration += new_lecture.duration

    def _get_hh_mm_from_timedelta(self, delta):
        total_seconds = delta.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        return hours, minutes

    def total(self):
        hours, minutes = self._get_hh_mm_from_timedelta(self._total_duration)
        return f"{hours:02d}:{minutes:02d}"
    
    def longest_lecture(self):
        longest = sorted(self.lectures, key=lambda x: x.duration)[-1]
        hours, minutes = self._get_hh_mm_from_timedelta(longest.duration)
        return f"{hours:02d}:{minutes:02d}"
    
    def longest_break(self):
        longest = timedelta(minutes=0)
        lectures = sorted(self.lectures, key=lambda x: x.start_time)
        if len(lectures) > 1:
            longest = lectures[1].start_time - lectures[0].end_time
            for i in range(2, len(self.lectures)):
                if longest < lectures[i].start_time - lectures[i-1].end_time:
                    longest = lectures[i].start_time - lectures[i-1].end_time
        hours, minutes = self._get_hh_mm_from_timedelta(longest)
        return f"{hours:02d}:{minutes:02d}"
