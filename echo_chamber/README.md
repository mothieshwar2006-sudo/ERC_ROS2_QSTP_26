# Echo Chamber — Week 0

ROS2 pub/sub assignment for ERC QSTP 2026.

## Nodes
- **talker**: publishes a random float (0-100) on `/random_number` at 1 Hz
- **listener**: subscribes to `/random_number`, multiplies by 2, logs result

## Run
```bash
ros2 run echo_chamber talker
ros2 run echo_chamber listener
```
