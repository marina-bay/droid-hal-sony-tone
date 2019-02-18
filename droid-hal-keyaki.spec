# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device keyaki
%define vendor sony

%define rpm_device keyaki
%define rpm_vendor qualcomm

%define lunch_device aosp_h4413-user
%define droid_target_aarch64 1

%define have_custom_img_boot 1
%define have_custom_img_recovery 1

# from https://github.com/mer-hybris/droid-hal-hammerhead/blob/ca102d255f1b6f274e2768e8cbd4ad9c631890e9/droid-hal-hammerhead.spec#L12
%define installable_zip 1
%define enable_kernel_update 1

# from https://github.com/mer-hybris/droid-hal-hammerhead/blob/ca102d255f1b6f274e2768e8cbd4ad9c631890e9/droid-hal-hammerhead.spec#L12
#define installable_zip 1
#define enable_kernel_update 1

%define pre_actions sudo update-java-alternatives -s java-1.8.0-openjdk-amd64

%define straggler_files\
    /bugreports\
    /d\
    /dsp\
    /nonplat_file_contexts\
    /nonplat_hwservice_contexts\
    /nonplat_property_contexts\
    /nonplat_seapp_contexts\
    /nonplat_service_contexts\
    /plat_file_contexts\
    /plat_hwservice_contexts\
    /plat_property_contexts\
    /plat_seapp_contexts\
    /plat_service_contexts\
    /sdcard\
    /cache\
    /vndservice_contexts\
    /verity_key\
    /vendor\
%{nil}

# want adreno quirks is required for browser at least, and other subtle issues
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

# Community builds may use the system partition for now
# TODO: Define this for community builds as well!
# Explanation: skips *mountpoints* from the fstab of device-sony-<device>
# This means no system <mountpoint>.mount file will get generated
# Important: nile is system-as-root, so "/" needs to be skipped to not generate
# a -.mount file
# For tone, /system needs to be added! Else a system.mount unit will be created
# that tries to mount /dev/block/bootdevice/by-name/system over /system!
#if 0%{?_obs_build_project:1}
# On Android 8 the system partition is (intended to be) mounted on /.
%define makefstab_skip_entries / /system /vendor /dev/stune /dev/cpuset /sys/fs/pstore /dev/cpuctl
Requires: droid-system
Requires: droid-system-vendor
#endif

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

