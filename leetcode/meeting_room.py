
# https://leetcode.com/problems/meeting-rooms/description/
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        interval_dict = {}
        for meeting in intervals:
            if meeting.start not in interval_dict:
                interval_dict[meeting.start] = meeting
            else:
                return False
        sorted_meetings = sorted(interval_dict.keys())
        for index in range(len(sorted_meetings) - 1):
            current_time = sorted_meetings[index]
            next_time = sorted_meetings[index + 1]
            if interval_dict[next_time].start != interval_dict[current_time].start:
                if interval_dict[current_time].end > interval_dict[next_time].start:
                    return False
            else:
                return False
        return True 
