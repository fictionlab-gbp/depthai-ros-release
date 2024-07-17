%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-depthai-examples
Version:        2.9.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS depthai_examples package

License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       opencv-devel
Requires:       ros-jazzy-camera-info-manager
Requires:       ros-jazzy-cv-bridge
Requires:       ros-jazzy-depth-image-proc
Requires:       ros-jazzy-depthai
Requires:       ros-jazzy-depthai-bridge
Requires:       ros-jazzy-depthai-descriptions
Requires:       ros-jazzy-depthai-ros-msgs
Requires:       ros-jazzy-foxglove-msgs
Requires:       ros-jazzy-image-transport
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-robot-state-publisher
Requires:       ros-jazzy-ros-environment
Requires:       ros-jazzy-rviz-imu-plugin
Requires:       ros-jazzy-sensor-msgs
Requires:       ros-jazzy-std-msgs
Requires:       ros-jazzy-stereo-msgs
Requires:       ros-jazzy-vision-msgs
Requires:       ros-jazzy-xacro
Requires:       ros-jazzy-ros-workspace
BuildRequires:  opencv-devel
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-camera-info-manager
BuildRequires:  ros-jazzy-cv-bridge
BuildRequires:  ros-jazzy-depthai
BuildRequires:  ros-jazzy-depthai-bridge
BuildRequires:  ros-jazzy-depthai-descriptions
BuildRequires:  ros-jazzy-depthai-ros-msgs
BuildRequires:  ros-jazzy-foxglove-msgs
BuildRequires:  ros-jazzy-image-transport
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-ros-environment
BuildRequires:  ros-jazzy-rviz-imu-plugin
BuildRequires:  ros-jazzy-sensor-msgs
BuildRequires:  ros-jazzy-std-msgs
BuildRequires:  ros-jazzy-stereo-msgs
BuildRequires:  ros-jazzy-vision-msgs
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The depthai_examples package

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Wed Jul 17 2024 sachin <sachin@luxonis.com> - 2.9.0-1
- Autogenerated by Bloom

