# Intervals And Heaps

## Drill

- Merge Intervals
- Meeting Rooms
- Meeting Rooms II / coordinator count
- Top K Frequent Elements
- K Closest Points

## Key Invariant

For meeting-room style problems, a min-heap of end times tracks the sessions
currently occupying resources. Pop while the earliest end time is less than or
equal to the current start time.
