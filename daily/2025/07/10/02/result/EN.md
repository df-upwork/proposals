1) Sending `VISION_POSITION_ESTIMATE` to the Extended Kalman Filter (EKF) while in `GUIDED_NOGPS` mode is incorrect and will not affect the quadcopter's position hold:
1.1) `VISION_POSITION_ESTIMATE` is intended to transmit position data directly to the EKF in the flight controller from an external system (e.g., a visual odometry system).
The EKF then combines these external data with readings from the inertial sensors (Inertial Measurement Unit, IMU) to estimate the quadcopter's position and velocity.
The flight controller then uses this estimate for autonomous position hold in modes such as `Loiter` or `Guided`.
To operate in this scenario without a physical GPS module, the EKF parameters must be configured to use an external navigation source.
1.2) The `GUIDED_NOGPS` flight mode does not use position or velocity data for stabilization and exclusively accepts commands to set the attitude (`SET_ATTITUDE_TARGET`).
This mode was developed to give companion computers low-level control over the quadcopter's attitude (similar to how a pilot controls it in `Stabilize` or `AltHold` modes).
The simplicity is evident in the source code:  https://github.com/ArduPilot/ardupilot/blob/master/ArduCopter/mode_guided_nogps.cpp
It calls the angle control handler, effectively making it a transparent channel for attitude commands. 
2) For the position hold task, applying a simple single-loop PID controller often leads to instability, oscillations, and overshoot.
A more reliable approach is the use of a cascaded (multi-loop) control architecture:
2.1) The outer loop (the position controller) converts the position error (the difference between the target and current position) into a target velocity.
If the quadcopter is to the right of the target, the controller generates a command to move to the left at a certain velocity.
The magnitude of this velocity is proportional to the distance from the target.
The input to this loop is the position error , and the output is the target velocity vector.
2.2) The inner loop (the velocity controller) minimizes the velocity error (the difference between the target and current velocity).
To change the velocity, an acceleration must be applied.
Thus, the input to this loop is the velocity error, and the output is the target acceleration vector.
3) For the specific task of holding the quadcopter at a single point (where the target velocity is zero), the architecture of point 2 can be simplified to a single PID controller operating on the position error:
3.1) The proportional term (`P`) responds to the current position error: `Output_P = Kp * error`. 
It provides the main restoring force toward the target.
3.2) The derivative term (`D`) reacts to the rate of change of the error, which is equivalent to counteracting the current velocity of the quadcopter: `Output_D = Kd * d(error)/dt`. 
It provides damping to prevent overshoot and oscillations.
3.3) The integral term (`I`) accumulates the error over time: `Output_I = Ki * integral(error)`. 
It compensates for constant external disturbances (e.g., wind) or systematic errors (e.g., imperfect calibration), which lead to static errors (e.g., when the quadcopter hovers slightly off the target).
3.4) The final output of the PID controllers for each of the horizontal axes (`X` and `Y`) is the desired acceleration `[ax, ay]`, which must be provided to the quadcopter to return it to the target point.
4) The PID controller from point 3 issues an abstract acceleration command, but a quadcopter is controlled by changing its orientation in space.
Therefore, a transformation step (based on the laws of dynamics) is necessary.
A quadcopter creates a lift force mainly directed along its vertical axis (`Z`).
To create horizontal acceleration, it must tilt (create roll or pitch), directing part of the thrust vector into the horizontal plane.
The target roll and pitch can be calculated from `[ax, ay]`:
```
roll = asin(ay / acceleration)
pitch = -asin(ax / acceleration)
```
The resulting Euler angles (roll and pitch) and the desired yaw angle (which can be considered constant, e.g., 0°, for the position hold task to maintain the heading) must be converted into a quaternion (as required by `SET_ATTITUDE_TARGET`).
5) Since in your case the position data arrives intermittently, a naive PID implementation will cause 2 problems:
5.1) A sudden loss of data can cause the integral term to grow excessively, leading to a large overshoot when the data returns.
5.2) The abrupt arrival of a new position after a pause will create a spike in the derivative term, resulting in sharp, jerky movements of the quadcopter.
6) The correct solution to point 5 is to continuously monitor the timestamp of the last received position message.
If the time since the last message exceeds a predefined threshold, the controller must enter a safe mode (e.g., hold its current attitude) and suspend PID updates until the data feed stabilizes. 