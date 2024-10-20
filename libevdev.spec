%define lib_major 2
%define lib_name %mklibname evdev %{lib_major}
%define develname %mklibname -d evdev

Name:		libevdev
Version:	1.13.3
Release:	1
Summary:	Kernel Evdev Device Wrapper Library
Group:		System/Libraries
License:	MIT
URL:		https://www.freedesktop.org/wiki/Software/libevdev
Source0:	http://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	meson

%description
%{name} is a library to wrap kernel evdev devices and provide a proper API
to interact with those devices.

%package -n evdev-utils
Summary:	Utilities for %{name}
Group:		System/Base

%description -n evdev-utils
%{name} is a library to wrap kernel evdev devices and provide a proper API
to interact with those devices.

%package -n %{lib_name}
Summary:	Kernel Evdev Device Wrapper Library
Group:		System/Libraries

%description -n %{lib_name}
%{name} is a library to wrap kernel evdev devices and provide a proper API
to interact with those devices.

%package -n %{develname}
Summary:	Kernel Evdev Device Wrapper Library Development Package
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}-%{release}

%description -n %{develname}
Kernel Evdev Device Wrapper Library Development Package.

%prep
%autosetup -p1

%build
%meson -Dtests=disabled -Ddocumentation=disabled -Dcoverity=false
%meson_build

%install
%meson_install

# We intentionally don't ship *.la files
find %{buildroot} -name "*.la" -delete

%files -n evdev-utils
%{_bindir}/libevdev-tweak-device
%{_bindir}/mouse-dpi-tool
%{_bindir}/touchpad-edge-detector

%files -n %{lib_name}
%{_libdir}/libevdev.so.%{lib_major}*

%files -n %{develname}
%doc COPYING
%{_includedir}/libevdev-1.0/
%{_libdir}/libevdev.so
%{_libdir}/pkgconfig/libevdev.pc
%doc %{_mandir}/man3/libevdev.3.*
%doc %{_mandir}/man1/*.1.*
