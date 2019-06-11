#ifndef STINGRAY_SRC_STINGRAY_DRIVERS_INCLUDE_TOPICSANDSERVICES_H_
#define STINGRAY_SRC_STINGRAY_DRIVERS_INCLUDE_TOPICSANDSERVICES_H_

#include <string>

static const std::string OUTPUT_PARCEL_TOPIC = "/stingray/topics/hardware_bridge/parcels";
static const std::string INPUT_PARCEL_TOPIC = "/stingray/topics/drivers/parcels";

static const std::string DEPTH_PUBLISH_TOPIC = "/stingray/topics/position/depth";

static const std::string GAZEBO_VELOCITY_TOPIC = "/cmd_vel";
static const std::string GAZEBO_ODOMETRY_PUBLISH_TOPIC = "/odom";

static const std::string SET_VELOCITY_SERVICE = "/stingray/services/control/set_velocity";
static const std::string SET_DEPTH_SERVICE = "/stingray/services/control/set_depth";
static const std::string SET_YAW_SERVICE = "/stingray/services/control/set_yaw";
static const std::string SET_IMU_ENABLED_SERVICE = "/stingray/services/control/set_imu_enabled";
static const std::string SET_STABILIZATION_SERVICE = "/stingray/services/control/set_stabilization";
static const std::string SET_DEVICE_SERVICE = "/stingray/services/control/set_device";

#endif //STINGRAY_SRC_STINGRAY_DRIVERS_INCLUDE_TOPICSANDSERVICES_H_