%global debug_package %{nil}
%global dkms_name wireguard

Name:           %{dkms_name}-dkms
Version:        0.0.20180513
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
dkms remove -m %{dkms_name} -v %{version} --all -q --rpm_safe_upgrade

%files
%{_usrsrc}/%{dkms_name}-%{version}

%changelog
* Sun May 13 2018 Joe Doss <joe@solidadmin.com> - 0.0.20180513-1
- Update to 0.0.20180513

* Fri Apr 20 2018 Joe Doss <joe@solidadmin.com> - 0.0.20180420-1
- Update to 0.0.20180420

* Sun Apr 15 2018 Joe Doss <joe@solidadmin.com> - 0.0.20180413-1
- Update to 0.0.20180413

* Mon Mar 05 2018 Joe Doss <joe@solidadmin.com> - 0.0.20180304-1
- Update to 0.0.20180304

* Mon Feb 19 2018 Joe Doss <joe@solidadmin.com> - 0.0.20180218-1
- Update to 0.0.20180218

* Sun Feb 04 2018 Joe Doss <joe@solidadmin.com> - 0.0.20180202-1
- Update to 0.0.20180202

* Thu Jan 18 2018 Joe Doss <joe@solidadmin.com> - 0.0.20180118-1
- Update to 0.0.20180118

* Thu Dec 21 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171221-1
- Update to 0.0.20171221

* Tue Dec 12 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171211-1
- Update to 0.0.20171211

* Mon Nov 27 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171127-1
- Update to 0.0.20171127

* Thu Nov 23 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171122-1
- Update to 0.0.20171122

* Sat Nov 11 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171111-1
- Update to 0.0.20171111

* Wed Nov 01 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171101-1
- Update to 0.0.20171101

* Thu Oct 26 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171017-1
- Update to 0.0.20171017

* Wed Oct 11 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171011-1
- Update to 0.0.20171011

* Fri Oct 6 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171005-1
- Update to 0.0.20171005
- Update RPM spec URL to www.wireguard.com

* Mon Oct 2 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171001-1
- Update to 0.0.20171001

* Mon Sep 18 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170918-1
- Update to 0.0.20170918
- Drop support for RHEL 7.3, moving on instead to RHEL 7.4.

* Thu Sep 7 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170907-1
- Update to 0.0.20170907

* Wed Aug 9 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170810-1
- Update to 0.0.20170810

* Mon Jul 31 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170726-1
- Update to 0.0.20170726

* Thu Jul 6 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170706-1
- Update to 0.0.20170706

* Fri Jun 30 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170629-2
- Remove elfutils-libelf-devel as a dependancy
- Add kernel-devel as a dependancy

* Thu Jun 29 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170629-1
- Update to 0.0.20170629
- Add elfutils-libelf-devel as a dependancy

* Tue Jun 13 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170613-1
- Update to 0.0.20170613

* Mon Jun 12 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170612-1
- Update to 0.0.20170612

* Wed May 31 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170531-1
- Update to 0.0.20170531

* Wed May 17 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170517-1
- Update to 0.0.20170517

* Mon Apr 24 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170421-1
- Update to 0.0.20170421

* Mon Apr 10 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170409-1
- Update to 0.0.20170409

* Fri Mar 24 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170324-1
- Update to 0.0.20170324

* Mon Mar 20 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170320.1-1
- Update to 0.0.20170320.1

* Thu Mar 2 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170223-1
- Update to 0.0.20170223

* Thu Feb 16 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170214-1
- Update to 0.0.20170214

* Thu Jan 5 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170105-1
- Update to 0.0.20170105

* Mon Dec 19 2016 Jason A. Donenfeld <jason@zx2c4.com> - 0.0.20161218-1
- Spec adjustments

* Wed Aug 17 2016 Joe Doss <joe@solidadmin.com> - 0.0.20160808-2
- Spec adjustments

* Mon Aug 15 2016 Joe Doss <joe@solidadmin.com> - 0.0.20160808-2
- Initial WireGuard DKMS RPM
- Version 0.0.20160808