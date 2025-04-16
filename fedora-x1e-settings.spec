Name: fedora-x1e-settings
Version: 1
Release: 1%{?dist}
Summary: Settings for Fedora on Qualcomm X Elite arm64 laptops
BuildArch: aarch64
License: GPLv2+
URL: https://github.com/Radiicall/fedora-x1e-settings
Source0: 55-x1e.conf
Source1: module-setup.sh
Source2: LICENSE
Requires: fedora-x1e-settings-dracut

%package dracut
Summary: dracut settings for Fedora on Qualcomm X Elite arm64 laptops
Requires: dracut

%description
This package provides default settings for Qualcomm X Elite devices on Fedora

%description dracut
Adds Qualcomm X Elite kmodules and firmware to dracut

%prep
cp $RPM_SOURCE_DIR/55-x1e.conf .
cp $RPM_SOURCE_DIR/module-setup.sh .
cp $RPM_SOURCE_DIR/LICENSE .
mkdir -p %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d/
mkdir -p %{buildroot}%{_prefix}/lib/dracut/modules.d/99x1e-firmware/

%build

%install
install -Dm644 55-x1e.conf %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d/55-x1e.conf
install -Dm755 module-setup.sh %{buildroot}%{_prefix}/lib/dracut/modules.d/99x1e-firmware/module-setup.sh

%files dracut
%{_prefix}/lib/dracut/dracut.conf.d/55-x1e.conf
%{_prefix}/lib/dracut/modules.d/99x1e-firmware/module-setup.sh

%files
%license LICENSE

%post dracut
dracut --force --regenerate-all

%changelog
* Wed Apr 16 2025 Radical <radical@radical.fun> - 1
  * Initial release