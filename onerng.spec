Summary:            Scripts for using the OneRNG entropy generator
Name:               onerng
Version:            3.6
Release:            1%{?dist}
License:            GPLv2+
Source:		    %{name}_%{version}.tgz
URL:                http://onerng.info/
BuildArch:	    noarch
Group:              System Environment/Base
BuildRequires:      rng-tools
BuildRequires:      udev
BuildRequires:      python
BuildRequires:      python-gnupg
BuildRequires:      gnupg
BuildRequires:      openssl
BuildRequires:      at

%description
The OneRNG entropy generator is a USB dongle that creates a stream of
data suitable for feeding to you kernel's entropy service. The device
does not need a special kernel driver.

This package installs a udev script that starts the rngd entropy daemon
when a OneRNG is plugged in.

%prep

%autosetup -n onerng_3.6

%build

%configure
make

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}/usr/lib/udev/rules.d  %{buildroot}/sbin %{buildroot}/etc
cp -f %{_builddir}/%{name}_%{version}/files/79-onerng.rules %{buildroot}/usr/lib/udev/rules.d/79-onerng.rules
cp -f %{_builddir}/%{name}_%{version}/files/onerng.sh %{buildroot}/sbin/onerng.sh
cp -f %{_builddir}/%{name}_%{version}/files/onerng_verify.py %{buildroot}/sbin/onerng_verify.py
cp -f %{_builddir}/%{name}_%{version}/files/onerng.conf %{buildroot}/etc/onerng.conf
chmod +x  %{buildroot}/sbin/onerng.sh
chmod +x  %{buildroot}/etc/onerng.conf
chmod +x  %{buildroot}/sbin/onerng_verify.py

%clean
rm -fr $RPM_BUILD_ROOT

%post
/usr/sbin/udevadm control --reload-rules
%postun
/usr/sbin/udevadm control --reload-rules
%files
%defattr(-,root,root)
%{_sbindir}/../../sbin/onerng.sh
%{_sbindir}/../../sbin/onerng_verify.py
%{_libdir}/../lib/udev/rules.d/79-onerng.rules
%{_sysconfdir}/onerng.conf


