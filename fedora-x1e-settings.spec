Name: fedora-x1e-settings
Version: 1
Release: 1%{?dist}
Summary: Settings for Fedora on Qualcomm X Elite arm64 laptops
BuildArch: aarch64
License: GPLv2+
URL: https://github.com/Radiicall/fedora-x1e-settings
Source0: 55-x1e.conf
Source1: module-setup.sh
Source2: grub-x1e-settings.cfg
Source3: LICENSE
Requires: fedora-x1e-settings-dracut, fedora-x1e-settings-grub2

%package dracut
Summary: dracut settings for Fedora on Qualcomm X Elite arm64 laptops
Requires: dracut

%package grub2
Summary: grub2 settings for Fedora on Qualcomm X Elite arm64 laptops
Requires: grub2

%description
This package provides default settings for Qualcomm X Elite devices on Fedora

%description grub2
Adds Qualcomm X Elite related boot arguments to grub2

%description dracut
Adds Qualcomm X Elite kmodules and firmware to dracut

%prep
cp $RPM_SOURCE_DIR/55-x1e.conf .
cp $RPM_SOURCE_DIR/module-setup.sh .
cp $RPM_SOURCE_DIR/grub-x1e-settings.cfg .
cp $RPM_SOURCE_DIR/LICENSE .
mkdir -p %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d/
mkdir -p %{buildroot}%{_prefix}/lib/dracut/modules.d/99x1e-firmware/
mkdir -p %{buildroot}/etc/default/grub.d

%build

%install
install -Dm644 55-x1e.conf %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d/55-x1e.conf
install -Dm755 module-setup.sh %{buildroot}%{_prefix}/lib/dracut/modules.d/99x1e-firmware/module-setup.sh
install -Dm644 grub-x1e-settings.cfg %{buildroot}/etc/default/grub.d/grub-x1e-settings.cfg

%files dracut
%{_prefix}/lib/dracut/dracut.conf.d/55-x1e.conf
%{_prefix}/lib/dracut/modules.d/99x1e-firmware/module-setup.sh

%files grub2

%files
%license LICENSE

%post dracut
dracut --force --regenerate-all

%post grub2
grub2-mkconfig -o "$(readlink -e /etc/grub2.cfg)"

%changelog
* Wed Apr 16 2025 Radical <radical@radical.fun> - 1
  * Initial release