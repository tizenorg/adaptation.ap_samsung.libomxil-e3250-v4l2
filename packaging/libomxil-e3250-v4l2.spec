Name: libomxil-e3250-v4l2
Summary: OpenMAX IL for e3250-v4l2
Version: 0.0.12
License: APLv2.0
Group: Development/Libraries
Release: 1
ExclusiveArch: %arm
Source: %{name}-%{version}.tar.gz

%description
implementation of OpenMAX IL for e3250-v4l2

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_libdir}/omx
mkdir -p %{buildroot}/usr/share/license
cp lib/lib*.so* %{buildroot}/%{_libdir}/ -r
cp lib/omx/lib*.so* %{buildroot}/%{_libdir}/omx/ -r
cp COPYING %{buildroot}/usr/share/license/%{name}

%post

%postun

%files
%manifest libomxil-e3250-v4l2.manifest
%{_libdir}/*.so*
%{_libdir}/omx/*.so*
/usr/share/license/%{name}

