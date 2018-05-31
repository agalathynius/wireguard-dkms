%global debug_package %{nil}
%global dkms_name wireguard

Name:           %{dkms_name}-dkms
Version:        0.0.20180531
Release:        1%{?dist}
Epoch:          1
URL:            https://www.wireguard.com/
Summary:        Fast, modern, secure VPN tunnel
License:        GPLv2
Group:          System Environment/Kernel
BuildArch:      noarch

Source0:        https://git.zx2c4.com/WireGuard/snapshot/WireGuard-%{version}.tar.xz

BuildRequires:  kernel-devel
BuildRequires:  sed

Provides:       %{dkms_name}-kmod = %{epoch}:%{version}-%{release}
Requires:       dkms
Requires:       kernel-devel

%description
WireGuard is a novel VPN that runs inside the Linux Kernel and uses
state-of-the-art cryptography (the "Noise" protocol). It aims to be
faster, simpler, leaner, and more useful than IPSec, while avoiding
the massive headache. It intends to be considerably more performant
than OpenVPN. WireGuard is designed as a general purpose VPN for
running on embedded interfaces and super computers alike, fit for
many different circumstances. It runs over UDP.

%prep
%setup -q -n WireGuard-%{version}

# Fix the Makefile for CentOS7 since it ships coreutils from 2013.
sed -i 's/install .* -D -t\(.\+\) /mkdir -p \1 \&\& \0/' %{_builddir}/WireGuard-%{version}/src/Makefile

%build

%install
mkdir -p %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/
make DESTDIR=%{buildroot} DKMSDIR=%{_usrsrc}/%{dkms_name}-%{version}/ -C %{_builddir}/WireGuard-%{version}/src dkms-install

%post
dkms add -m %{dkms_name} -v %{version} -q --rpm_safe_upgrade
dkms build -m %{dkms_name} -v %{version} -q
dkms install -m %{dkms_name} -v %{version} -q

%preun
dkms remove -m %{dkms_name} -v %{version} --all -q --rpm_safe_upgrade || :

%files
%{_usrsrc}/%{dkms_name}-%{version}

%changelog
